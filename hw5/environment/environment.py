import random
import numpy as np
import gymnasium as gym
from gymnasium import spaces
from collections import deque

class ServiceEnv(gym.Env):
    """
    服務排隊環境 v12 多隊列版本 + 動態資源切片 + 拆分動作
    支援:
        - 不同類別的 service time
        - 最大 queue 長度 queue_maxlen
        - next_class one-hot encoding
        - 每種服務獨立隊列及其滿隊列懲罰
        - 狀態中加入每個切片佇列長度與當前 capacity
        - 動態增減伺服器槽 (resource scaling)
        - 動作拆分：scaling 與 admission control
        - 以 duration 控制 episode 長度
    Observation:
        [active_servers]
        + [served_counts_per_class...]
        + [queue_lengths...]
        + [one_hot_next_class]
        + [capacity]
    Action:
        MultiDiscrete([2*Δ+1, 2])  # scaling_action, admit_action
        scaling_action: 0->-Δ, Δ->0, 2Δ->+Δ
        admit_action: 0=reject, 1=accept
    """
    metadata = {"render_modes": ["human"]}

    def __init__(
                 self,
                 lams,
                 mu,
                 capacity,
                 max_capacity=None,
                 scaling_delta=1,
                 duration=None,
                 lambda_per_step=1.0,
                 reward_scheme=None,
                 reject_penalty_scheme=None,
                 seed_val=None,
                 queue_maxlen=10):
        super().__init__()
        self.lams = lams
        self.mu_list = mu if isinstance(mu, list) else [mu] * len(lams)
        # 初始與最大 capacity
        self.capacity = capacity
        self.max_capacity = max_capacity if max_capacity is not None else capacity
        self.scaling_delta = scaling_delta
        # episode 長度由 duration 控制，若未提供則 default 200
        self.max_episode_steps = int(duration) if duration is not None else 200

        self.queue_maxlen = queue_maxlen
        self.lambda_per_step = lambda_per_step
        self.reward_scheme = reward_scheme or [1] * len(lams)
        self.reject_penalty_scheme = reject_penalty_scheme or [-1] * len(lams)
        self.n_classes = len(self.mu_list)

        # observation 維度: 1 + n_classes + n_classes + n_classes + 1(capacity)
        obs_dim = 1 + self.n_classes + self.n_classes + self.n_classes + 1
        self.observation_space = spaces.Box(
            low=0,
            high=np.inf,
            shape=(obs_dim,),
            dtype=np.int32
        )
        # 動作空間：拆分 scaling 與 admission control
        self.action_space = spaces.MultiDiscrete([2 * self.scaling_delta + 1, 2])

        # 內部狀態
        self.server_slots = None
        self.queues = None
        self.counts = None
        self.current_class = None
        self.has_arrival = False
        self.state = None
        self.current_step = 0
        self.episode_step = 0

        # 可複製環境
        if seed_val is not None:
            random.seed(seed_val)
            np.random.seed(seed_val)

        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        # 初始化 server_slots
        self.server_slots = [0] * self.capacity
        self.queues = [deque(maxlen=self.queue_maxlen) for _ in range(self.n_classes)]
        self.counts = [0 for _ in range(self.n_classes)]
        self.current_step = 0
        self.episode_step = 0
        self.has_arrival = False
        self.current_class = None
        # 首次到達
        self._generate_arrival()
        self._update_state()
        return self.state, {}

    def _generate_arrival(self):
        if random.random() < self.lambda_per_step:
            self.has_arrival = True
            self.current_class = random.choices(
                range(self.n_classes), weights=self.lams)[0]
        else:
            self.has_arrival = False
            self.current_class = -1

    def _encode_next_class(self):
        vec = [0] * self.n_classes
        if self.has_arrival and 0 <= self.current_class < self.n_classes:
            vec[self.current_class] = 1
        return vec

    def _update_state(self):
        active = sum(1 for t in self.server_slots if t > 0)
        queue_lengths = [len(q) for q in self.queues]
        self.state = np.array(
            [active] + self.counts + queue_lengths + self._encode_next_class() + [self.capacity],
            dtype=np.int32
        )

    def _assign_to_server(self, service_time: int) -> bool:
        for i in range(len(self.server_slots)):
            if self.server_slots[i] == 0:
                self.server_slots[i] = service_time
                return True
        return False

    def _scale_capacity(self, delta: int):
        new_cap = int(np.clip(self.capacity + delta, 0, self.max_capacity))
        if new_cap == self.capacity:
            return
        if new_cap > self.capacity:
            self.server_slots.extend([0] * (new_cap - self.capacity))
        else:
            remove_count = self.capacity - new_cap
            free_slots = [i for i, t in enumerate(self.server_slots) if t == 0]
            for idx in reversed(free_slots[:remove_count]):
                self.server_slots.pop(idx)
        self.capacity = new_cap

    def step(self, action):
        self.current_step += 1
        self.episode_step += 1
        # 解析動作：scaling_action, admit_action
        scaling_action, admit_action = action
        # 資源 scaling
        delta = scaling_action - self.scaling_delta
        self._scale_capacity(delta)
        # 服務時間倒數
        self.server_slots = [max(0, t - 1) for t in self.server_slots]
        # 佇列→伺服器 調度
        for cls in range(self.n_classes):
            q = self.queues[cls]
            while q:
                service_time = max(1, int(random.expovariate(self.mu_list[cls])))
                if self._assign_to_server(service_time):
                    self.counts[cls] += 1
                    q.popleft()
                else:
                    break
        # Admission Control 與獎勵
        reward = 0
        if self.has_arrival:
            cls = self.current_class
            if admit_action == 1:
                st = max(1, int(random.expovariate(self.mu_list[cls])))
                if self._assign_to_server(st):
                    self.counts[cls] += 1
                    reward = self.reward_scheme[cls]
                elif len(self.queues[cls]) < self.queue_maxlen:
                    self.queues[cls].append(cls)
                else:
                    reward = self.reject_penalty_scheme[cls]
            else:
                reward = self.reject_penalty_scheme[cls]
        # 下一到達與狀態更新
        self._generate_arrival()
        self._update_state()
        done = (self.episode_step >= self.max_episode_steps)
        return self.state, reward, done, False, {}

    def render(self):
        next_c = self.current_class if self.has_arrival else None
        qs = [len(q) for q in self.queues]
        print(f"[Step {self.current_step}] "
              f"Capacity: {self.capacity}, "
              f"Servers: {self.server_slots}, "
              f"Queues: {qs}, "
              f"Counts: {self.counts}, "
              f"Next: {next_c}")

import sys, os, shutil

# 把项目根目录（scripts 的上一级）加到模块搜索路径
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import torch
import argparse
import yaml
from environment.environment_v12 import ServiceEnv
from stable_baselines3 import DQN
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.monitor import Monitor
import numpy as np
import gymnasium as gym
from gymnasium import spaces
from gymnasium.core import Wrapper
from gymnasium import spaces

# 自訂 FlattenMultiDiscrete Wrapper
class FlattenMultiDiscrete(Wrapper):
    def __init__(self, env):
        super().__init__(env)
        if not isinstance(env.action_space, spaces.MultiDiscrete):
            raise ValueError("FlattenMultiDiscrete only works with MultiDiscrete action spaces")
        self.orig_nvec = env.action_space.nvec.copy()
        # 總 action 數 = product of nvec
        self.action_space = spaces.Discrete(int(np.prod(self.orig_nvec)))

    def reset(self, **kwargs):
        obs, info = self.env.reset(**kwargs)
        return obs, info

    def step(self, action):
        # decode single integer to multi-dimensional action
        indices = np.unravel_index(action, self.orig_nvec)
        multi_action = np.array(indices)
        return self.env.step(multi_action)

# 將專案根目錄加入模組路徑
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


def run_training(config_path: str, run_id: int):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[INFO] Using device: {device.upper()}")

    # 讀取配置
    print(f"[INFO] Loading configuration from {config_path}")
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    print(f"[INFO] Config loaded: {config}")

    # 環境建立
    env_cfg = config.get('env', {})
    raw_env = ServiceEnv(**env_cfg)
    # 使用自訂 FlattenMultiDiscrete 將 MultiDiscrete 轉 Discrete
    flat_env = FlattenMultiDiscrete(raw_env)

    trainer_cfg = config.get('trainer', {})
    log_dir = trainer_cfg.get('log_dir', 'logs/')
    os.makedirs(log_dir, exist_ok=True)

    # Monitor 包裝
    monitor_filename = trainer_cfg.get('monitor_filename', f'monitor_run{run_id}.csv')
    monitor_path = os.path.join(log_dir, monitor_filename)
    os.makedirs(os.path.dirname(monitor_path), exist_ok=True)
    env = Monitor(flat_env, filename=monitor_path)

    # TensorBoard
    tb_folder = trainer_cfg.get('tb_log_folder', 'tensorboard/')
    tb_log_path = os.path.join(log_dir, tb_folder)
    os.makedirs(tb_log_path, exist_ok=True)

    print(f"[INFO] Logs directory: {log_dir}")
    print(f"[INFO] Monitor logs: {monitor_path}")
    print(f"[INFO] TensorBoard logs: {tb_log_path}")

    # Agent 建構
    agent_cfg = config.get('agent', {})
    print(f"[INFO] Agent config: {agent_cfg}")
    model = DQN(
        policy=agent_cfg.get('policy', 'MlpPolicy'),
        env=env,
        learning_rate=float(agent_cfg.get('learning_rate', 1e-3)),
        buffer_size=int(agent_cfg.get('buffer_size', 50_000)),
        learning_starts=int(agent_cfg.get('learning_starts', 1_000)),
        batch_size=int(agent_cfg.get('batch_size', 64)),
        gamma=float(agent_cfg.get('gamma', 0.99)),
        train_freq=int(agent_cfg.get('train_freq', 1)),
        target_update_interval=int(agent_cfg.get('target_update_interval', 1_000)),
        tensorboard_log=tb_log_path,
        verbose=0,
        device=device,
        exploration_initial_eps=agent_cfg.get('exploration_initial_eps', 1.0),
        exploration_final_eps=agent_cfg.get('exploration_final_eps', 0.05),
        exploration_fraction=agent_cfg.get('exploration_fraction', 0.1),
    )

    # 評估回調
    save_freq = int(trainer_cfg.get('save_freq', 10_000))
    eval_cb = EvalCallback(
        env,
        best_model_save_path=log_dir,
        log_path=log_dir,
        eval_freq=save_freq,
        deterministic=True,
        render=False
    )
    print(f"[INFO] Evaluation every {save_freq} steps")

    # 開始訓練
    total_timesteps = int(trainer_cfg.get('total_timesteps', 200_000))
    log_interval = int(trainer_cfg.get('log_interval', 4))
    print(f"[INFO] Starting training for {total_timesteps} timesteps")
    model.learn(
        total_timesteps=total_timesteps,
        callback=eval_cb,
        log_interval=log_interval
    )
    print("[INFO] Training finished")

    # 保存模型
    save_path = trainer_cfg.get('save_path', 'dqn_service_queue')
    final_path = os.path.join(log_dir, f"{save_path}_run{run_id}")
    model.save(final_path)
    print(f"[INFO] Final model saved to: {final_path}.zip")


if __name__ == '__main__':
    import time
    parser = argparse.ArgumentParser(description="Train DQN on ServiceEnv")
    parser.add_argument('--config', type=str, default='config_v6.yaml', help='Path to configuration file')
    parser.add_argument('--n_runs', type=int, default=1, help='Number of training runs')
    args = parser.parse_args()

    # 刪除舊 logs
    default_log_dir = 'logs'
    if os.path.exists(default_log_dir):
        print(f"[INFO] Removing existing logs directory: {default_log_dir}")
        shutil.rmtree(default_log_dir)

    for run_id in range(args.n_runs):
        print(f"\n[RUN {run_id+1}/{args.n_runs}] Starting training...\n")
        run_training(args.config, run_id)
        time.sleep(1)

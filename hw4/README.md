# HW4 DQN and its variants

## 🧠 HW4-1: Naive DQN  for static mode[30%]

### ✅ Run the provided code naive or Experience buffer reply 

- [程式碼檔案](hw4-1/hw4-1.ipynb)

### 💬 Chat with ChatGPT about the code to clarify your understanding

<img src="/hw4/static/hw4-1.png" alt="Chat with ChatGPT" width="400"/>

### 📝 Submit a short understanding report

#### 導言
本筆記本示範如何在 Gridworld 環境（一個經典的強化學習問題）中實作深度 Q 網路 (DQN)。DQN 是一種基於價值的強化學習演算法，使用深度神經網路來近似 Q 值函數，使 agent 能在高維度狀態空間中學習最優策略。

#### 主要組成

1. Gridworld 環境

    * 一個簡單的 4×4 格子遊戲，agent 必須在避免陷阱的同時到達目標。
    * 環境提供狀態、獎勵，並支援上下左右四種動作。

2. 神經網路模型

    * Q 網路是一個多層感知器，將狀態作為輸入，輸出對應每個動作的 Q 值。
    * 使用均方誤差 (MSE) 損失函數，比較預測的 Q 值與目標 Q 值來訓練模型。

3. 訓練迴圈

    * agent 以 ε–貪婪策略與環境互動（探索 vs. 利用）。
    * 每執行一次動作後，agent 取得獎勵並更新 Q 網路。
    * 引入經驗回放和目標網路以穩定訓練並提升效能。

3. 經驗回放

    * 將過去的經驗存入緩衝區，並隨機抽取小批次進行訓練。
    * 幫助打破連續樣本之間的相關性，提升學習效率。

4. 目標網路

    * 使用一個獨立的網路來計算目標 Q 值，較少更新以降低過度估計的偏差。

5. 評估

    * 在 static 與 random 兩種 Gridworld 設定下測試訓練後的模型，以評估其效能與泛化能力。

#### 學習成果

- 了解 DQN 如何將 Q-Learning 與深度學習結合來解決強化學習問題。
- 掌握經驗回放和目標網路在穩定 DQN 訓練過程中的關鍵作用。
- 獲得在簡易環境中實作並調校 DQN 的實務經驗。

---

## ⚖️ HW4-2: Enhanced DQN Variants  for player  mode [40%]

### Compare Double DQN & Dueling DQN
💡 Focus on how they improve upon the basic DQN approach

### 1. **實驗設定**

- **環境**：  
  4×4 Gridworld（_player mode_）  
- **狀態維度**：16 格 × 4 通道 → 64  
- **動作空間**：↑ ↓ ← →（4）  
- **超參數**：  
  ```yaml
  γ: 0.9
  learning_rate: 1e-3
  ε-greedy: 從 1.0 → 0.1
  replay_buffer: 1000
  batch_size: 200
  target_update_freq: 每 1000 步
  episodes: 5000
  ```

* **評估指標**：

  1. **Loss**：移動平均 ±1 標準差（window=50）
  2. **Episode Reward**：移動平均 ±1 標準差（window=50）

---

### 2. **結果分析**

#### 2.1 **Loss 移動平均 ±1 標準差**

<figure>
  <img src="/hw4/static/hw4-2-1.png" alt="Loss Moving Avg ±1 std (window=50)" />
  <figcaption><em>圖1：損失隨梯度更新步數的移動平均 ±1 標準差（window=50）</em></figcaption>
</figure>

* **快速收斂**：三種變體皆在約 1 萬–2 萬 次更新內，Loss 降至接近 0。
* **震盪幅度**：

  * ***Basic DQN***（藍線）初期震盪最大。
  * ***Double DQN***（綠線）與 ***Dueling DQN***（紅線）略微抑制了初期波動。

#### 2.2 **每集獎勵移動平均 ±1 標準差**

<figure>
  <img src="/hw4/static/hw4-2-2.png" alt="Episode Reward Moving Avg ±1 std (window=50)" />
  <figcaption><em>圖2：累積獎勵隨 Episode 的移動平均 ±1 標準差（window=50）</em></figcaption>
</figure>

* **初始表現**：所有方法前 500 集平均獎勵約落在 –30 至 –10。
* **收斂速度**：

  * ***Dueling DQN***（紅線）約在 2000–3000 集開始穩定。
  * ***Double DQN***（綠線）次之，中期波動較小。
  * ***Basic DQN***（藍線）最慢，約 3000 集後才趨穩。
* **穩定性**：

  * 三者最終皆穩定在 +0…+10 區間。
  * **<mark>Dueling DQN</mark>** 的 ±1 標準差區間最窄，變異度最低。

---

### 3. **結論與建議**

1. **Loss 收斂**

   * 所有方法均能將 Loss 收斂至近零，說明此小型環境易於擬合貝爾曼更新。
2. **獎勵收斂與穩定性**

   * **<mark>Dueling DQN</mark>**：收斂最快、最穩定
   * **<mark>Double DQN</mark>**：有效抑制過度估計，結構簡單
   * **<mark>Basic DQN</mark>**：最簡單但收斂最慢
3. **推薦**

   * 追求 **快速且穩定** → ***Dueling DQN***
   * 需平衡 **估計偏差** 與 **結構簡潔** → ***Double DQN***

---

### 4. **未來工作**

* **擴充環境規模**：更大格子、更多隨機性 → 測試泛化能力
* **進階技巧**：優先回放 (Prioritized Replay)、軟更新 (soft‐update)、學習率調度
* **重複實驗**：多次獨立訓練 → 計算跨 run 之平均與變異，提升結果可信度

---

## 🔁 HW4-3: Enhance DQN for random mode WITH Training Tips [30%]

### Convert the DQN model from PyTorch to either:
Keras, or PyTorch Lightning

### Bonus points for integrating training techniques to stabilize/improve learning (e.g., gradient clipping, learning rate scheduling, etc.)
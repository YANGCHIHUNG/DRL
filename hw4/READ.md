# HW4 DQN and its variants

## 🧠 HW4-1: Naive DQN  for static mode[30%]

### ✅ Run the provided code naive or Experience buffer reply 

### 💬 Chat with ChatGPT about the code to clarify your understanding

![Chat with ChatGPT](/hw4/static/hw4-1.png)

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

## ⚖️ HW4-2: Enhanced DQN Variants  for player  mode [40%]

### Compare Double DQN & Dueling DQN
💡 Focus on how they improve upon the basic DQN approach

## 🔁 HW4-3: Enhance DQN for random mode WITH Training Tips [30%]

### Convert the DQN model from PyTorch to either:
Keras, or PyTorch Lightning

### Bonus points for integrating training techniques to stabilize/improve learning (e.g., gradient clipping, learning rate scheduling, etc.)
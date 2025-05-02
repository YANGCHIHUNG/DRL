# 多臂賭徒問題與常見演算法說明

## 使用者：解釋Arm-Bandit Problem
## 助理：

## 🎰 Multi-Armed Bandit Problem（多臂賭徒問題）

想像你在賭場面前有 K 部拉霸機（arm），每台機器的回報機率未知，每次只能選一台試玩。目標是在有限次數的操作中，最大化總回報。

### 數學定義：
- 臂數（arms）：K 條臂。
- 第 i 臂的期望回報：\mu_i。
- 最佳臂期望回報：\mu^* = max_i \mu_i。
- 累積遺憾（Regret）：
  \[
  R(T) = T \mu^* - \mathbb{E}\left[\sum_{t=1}^T X_{I_t,t}
ight]
  \]


---

## 使用者：解釋Epsilon Greedy
## 助理：

## 🎯 1. Epsilon-Greedy 演算法

### 步驟：
1. 設定 ε（例如 0.1）
2. 每一輪：
   - 以 ε 機率隨機探索
   - 以 1 - ε 機率選擇平均回報最高的 arm

### 優缺點：
- ✅ 簡單、易實作
- ❌ 探索率固定，長期無法自動調整

---

## 使用者：解釋UCB (Upper Confidence Bound)
## 助理：

## 📈 2. UCB（Upper Confidence Bound）演算法

### 選擇公式：
\[
	ext{UCB}_i(t) = ar{X}_i(t) + \sqrt{rac{2 \ln t}{N_i(t)}}
\]

- ar{X}_i(t)：arm i 的平均回報
- N_i(t)：arm i 被拉的次數
- t：目前的總時間步

### 優缺點：
- ✅ 無需 ε，探索與開採自動平衡
- ✅ 有理論保證 O(log T) regret
- ❌ 僅適用靜態分布，數值上需小心初始化


---

## 使用者：講解Softmax
## 助理：

## 🔥 3. Softmax 策略（Boltzmann Exploration）

### 概念：
- 根據每條 arm 的平均回報計算機率：
\[
P_i(t) = rac{e^{\hat{\mu}_i / 	au}}{\sum_{j=1}^{K} e^{\hat{\mu}_j / 	au}}
\]

- \(	au\)：溫度參數，越大越隨機、越小越貪婪。

### 優缺點：
- ✅ 用機率調控探索程度
- ❌ τ 參數敏感，需手動調整

---

## 使用者：介紹Thompson Samling
## 助理：

## 🧠 4. Thompson Sampling（貝葉斯策略）

### 運作方式（以 Bernoulli 分布為例）：
1. 每個 arm i 初始使用 Beta(a_i, b_i)
2. 每一輪：
   - 對每個 arm 抽樣 \(	heta_i \sim 	ext{Beta}(a_i, b_i)\)
   - 選擇最大的 θ_i 對應的 arm
   - 根據結果更新 a_i, b_i

### 優缺點：
- ✅ 探索與開採自然平衡
- ✅ 效能好，regret 低
- ❌ 需維護後驗分布，對非專家較不直覺


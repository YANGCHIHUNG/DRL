# Project Overview

This project is a web-based grid map application developed using Flask, HTML, CSS, and JavaScript. The application allows users to interactively generate a grid (with a dynamic size between 5 and 9), select a start cell (green), an end cell (red), and designate obstacles (gray). Additionally, it integrates basic reinforcement learning features by generating a random policy (with valid actions only) and evaluating state values using an iterative policy evaluation algorithm.

Below are the evaluation criteria along with their respective weightings:

## 1. 網格地圖功能完整性 Grid Map Functionality Completeness (30%)
- **動態網格生成：** 支援從 5x5 到 9x9 的網格尺寸。  
- **互動式格子選擇：** 使用者可以指定起點、終點及障礙物。  
- **視覺反饋：** 每個格子根據使用者操作正確更新其顯示。
- **Dynamic Grid Generation:** Supports grid sizes from 5x5 to 9x9.
- **Interactive Cell Selection:** Users can designate start, end, and obstacles.
- **Visual Feedback:** Each cell correctly updates its display based on user actions.

## 2. 使用者界面友好性 User Interface Friendliness (15%)
- **清晰指示：** 介面提供逐步操作指南，方便使用應用程式。  
- **直覺式控制：** 生成網格、重置及產生策略的按鈕設置易於使用。  
- **視覺指示：** 即時的視覺反饋（顏色變化與符號）提升使用者體驗。
- **Clear Instructions:** The UI provides step-by-step guidelines for using the application.
- **Intuitive Controls:** Buttons for creating the grid, resetting, and generating policies are easily accessible.
- **Visual Indicators:** Immediate visual feedback (color changes and symbols) enhances user experience.

## 3. 程式碼結構與可讀性 Code Structure and Readability (10%)
- **模組化組織：** 將 Flask 後端與前端代碼 HTML 分離。  
- **程式碼註解：** 附有完整註解，便於理解與維護。  
- **最佳實踐：** 遵循程式碼標準及慣例，以確保代碼清晰。
- **Modular Organization:** Separation between the Flask backend and front-end code (HTML, CSS, JavaScript).
- **Commented Code:** Well-documented code to aid in understanding and maintenance.
- **Best Practices:** Adherence to coding standards and practices to ensure clarity.

## 4. 網頁操作流暢度 Web Page Operation Smoothness (5%)
- **互動迅速：** 點擊格子、重置網格或生成策略時，過渡流暢。  
- **更新最佳化：** 高效處理 DOM 更新，避免明顯延遲。  
- **錯誤處理：** 對非預期使用者操作進行優雅處理。
- **Responsive Interactions:** Smooth transitions when clicking cells, resetting the grid, or generating policies.
- **Optimized Updates:** Efficient handling of DOM updates to avoid any noticeable delays.
- **Error Handling:** Graceful handling of unexpected user interactions.

## 5. 隨機生成行動顯示功能 Random Action Display Functionality (20%)
- **有效行動生成：** 僅在動作有效（不超出網格或進入障礙物）的情況下隨機分配箭頭。  
- **視覺呈現：** 每個非障礙物格子均清楚顯示選取的箭頭。  
- **無縫整合：** 隨機行動生成功能與網格互動特性完美整合。
- **Valid Action Generation:** Randomly assigns actions (arrows) only if the move is valid (does not go off-grid or into an obstacle).
- **Visual Representation:** Each cell (except obstacles) displays the chosen arrow clearly.
- **Seamless Integration:** The random action generation is fully integrated with the grid's interactive features.

## 6. 策略評估的正確性 Policy Evaluation Accuracy (15%)
- **迭代評估：** 使用折扣因子 (γ = 0.9) 的迭代算法計算狀態價值。  
- **正確處理：** 妥善管理終點狀態（終點格子值固定為 0）及障礙物。  
- **價值反映：** 計算出的狀態價值精確反映預期的強化學習模型。
- **Iterative Evaluation:** Uses an iterative algorithm with a discount factor (γ = 0.9) to compute state values.
- **Correct Handling:** Properly manages terminal states (end cell fixed at value 0) and obstacles.
- **Reflective Values:** The computed state values accurately reflect the intended reinforcement learning model.

## 7. 程式碼結構與可讀性 Additional Code Structure and Readability (5%)
- **工具函數：** 輔助工具函數以模組化方式組織。  
- **易於維護：** 程式碼結構便於未來更新與擴展。  
- **實作清晰：** 特別強調編寫清晰且簡潔的程式碼，以便未來增強功能。
- **Utility Functions:** Additional helper functions are organized for modularity.
- **Maintainability:** The code structure supports easy updates and scalability.
- **Clarity in Implementation:** Extra emphasis on writing clear and concise code for future enhancements.

---

# How to Use This Project

## Prerequisites
- **Python:** Make sure you have Python 3.8 or later installed.
- **Flask:** Install Flask using pip. For example, run:
  ```bash
  pip install Flask
  ```

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YANGCHIHUNG/DRL.git
   cd hw1
   ```
2. **(Optional) Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. **Start the Flask Server:**
   ```bash
   python app.py
   ```
2. **Open Your Web Browser:**
   Navigate to `http://127.0.0.1:5000` (or the specified address).

## Using the Application Interface
1. **Set Grid Size:**
   - Enter a grid size between 5 and 9 in the provided input field.
   - Click the "Create Grid" button to generate the grid.

2. **Configure the Grid:**
   - **Start Cell:** Click on any cell to set the start position (will turn green).
   - **End Cell:** Click on another cell to set the end position (will turn red).
   - **Obstacles:** Click on additional cells to mark obstacles (gray). You can mark up to `n-2` obstacles.

3. **Reinforcement Learning Features:**
   - Click the "Generate Random Policy and Evaluate State Values" button.
   - The application will generate a random, valid action (arrow) for each non-obstacle cell.
   - It will also evaluate the state value V(s) using an iterative policy evaluation process, displaying the arrow and the computed value in each cell.

4. **Reset the Grid:**
   - Click the "Reset" button to clear all selections and grid values. This allows you to reconfigure the grid as needed.

Enjoy exploring the grid map and experimenting with basic reinforcement learning functionalities!

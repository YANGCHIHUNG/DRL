# Project Overview and Evaluation Criteria

This project is a web-based grid map application developed using Flask, HTML, CSS, and JavaScript. The application allows users to interactively generate a grid (with a dynamic size between 5 and 9), select a start cell (green), an end cell (red), and designate obstacles (gray). Additionally, it integrates basic reinforcement learning features by generating a random policy (with valid actions only) and evaluating state values using an iterative policy evaluation algorithm.

Below are the evaluation criteria along with their respective weightings:

## 1. Grid Map Functionality Completeness (30%)
- **Dynamic Grid Generation:** Supports grid sizes from 5x5 to 9x9.
- **Interactive Cell Selection:** Users can designate start, end, and obstacles.
- **Visual Feedback:** Each cell correctly updates its display based on user actions.

## 2. User Interface Friendliness (15%)
- **Clear Instructions:** The UI provides step-by-step guidelines for using the application.
- **Intuitive Controls:** Buttons for creating the grid, resetting, and generating policies are easily accessible.
- **Visual Indicators:** Immediate visual feedback (color changes and symbols) enhances user experience.

## 3. Code Structure and Readability (10%)
- **Modular Organization:** Separation between the Flask backend and front-end code (HTML, CSS, JavaScript).
- **Commented Code:** Well-documented code to aid in understanding and maintenance.
- **Best Practices:** Adherence to coding standards and practices to ensure clarity.

## 4. Web Page Operation Smoothness (5%)
- **Responsive Interactions:** Smooth transitions when clicking cells, resetting the grid, or generating policies.
- **Optimized Updates:** Efficient handling of DOM updates to avoid any noticeable delays.
- **Error Handling:** Graceful handling of unexpected user interactions.

## 5. Random Action Display Functionality (20%)
- **Valid Action Generation:** Randomly assigns actions (arrows) only if the move is valid (does not go off-grid or into an obstacle).
- **Visual Representation:** Each cell (except obstacles) displays the chosen arrow clearly.
- **Seamless Integration:** The random action generation is fully integrated with the grid's interactive features.

## 6. Policy Evaluation Accuracy (15%)
- **Iterative Evaluation:** Uses an iterative algorithm with a discount factor (γ = 0.9) to compute state values.
- **Correct Handling:** Properly manages terminal states (end cell fixed at value 0) and obstacles.
- **Reflective Values:** The computed state values accurately reflect the intended reinforcement learning model.

## 7. Additional Code Structure and Readability (5%)
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
   git clone <repository_url>
   cd <repository_directory>
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

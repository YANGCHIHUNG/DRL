# <span style="color: #007BFF; font-weight: bold;">Grid Map with Value Iteration</span>

A **Flask-based web application** that allows users to interactively create an **nxn grid map**, designate a **start cell**, an **end cell**, and **obstacles**, and then compute the **optimal policy** using the **Value Iteration algorithm**.

## Demo
![Demo](static/demo.gif)

## Features

- **Interactive Grid Creation:**
  - **Choose a grid size** between **5 and 9**.
  - **Click** to set a **start cell** (<span style="color: green;">green</span>), an **end cell** (<span style="color: red;">red</span>), and up to **n-2 obstacles** (<span style="color: gray;">gray</span>).
- **Value Iteration Algorithm:**
  - **Computes optimal state values and policies** for each cell.
  - **Displays the optimal action** (arrow) and **state value** within each cell.
- **Optimal Path Animation:**
  - **Animates the optimal path** from the start to the end cell (excluding the start and end cells).
- **Refined User Interface:**
  - Enhanced design with **modern CSS**, a **responsive layout**, **smooth transitions**, and **Google Fonts (Roboto)**.

## Value Iteration Explanation

**Value Iteration** is a dynamic programming algorithm used to solve **Markov Decision Processes (MDPs)**. It iteratively updates the value of each state by applying the **Bellman optimality equation**:

```
V(s) = max_a [ R(s, a) + γ * V(s') ]
```

where:
- **`V(s)`** is the value of state **`s`**,
- **`R(s, a)`** is the immediate reward (in this project, a cost of **-1 per move**),
- **`γ` (gamma)** is the discount factor (set to **0.9**),
- **`V(s')`** is the value of the subsequent state after taking action **`a`**.

The algorithm repeatedly updates the state values until they converge or a set number of iterations is reached. The **optimal policy** is derived by choosing the action that **maximizes** the value function at each state. This process efficiently computes both the state values and the best actions even in the presence of obstacles and terminal states.

## Getting Started

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YANGCHIHUNG/DRL.git
   cd hw2
   ```
2. **Create and Activate a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application:**
   ```bash
   python app.py
   ```
5. **Access the Application:**
   Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

1. **Set the Grid Size:**  
   Specify a grid size between **5** and **9**, then click **"Create Grid"** to generate the grid.

2. **Configure the Grid:**  
   - Click a cell to set the **start point** (<span style="color: green; font-weight: bold;">green</span>).  
   - Click a different cell to set the **end point** (<span style="color: red; font-weight: bold;">red</span>).  
   - Click additional cells to mark **obstacles** (<span style="color: gray; font-weight: bold;">gray</span>) until you have selected up to **n-2 obstacles**.

3. **Compute the Optimal Policy:**  
   Click the **"Compute"** button to run the value iteration algorithm. Each cell will display the **optimal action** (arrow) and its computed **state value**.

4. **View the Optimal Path:**  
   The optimal path from the start to the end cell will be animated, with intermediate cells highlighted in **light green**.

5. **Reset the Grid:**  
   Click the **"Reset"** button to clear the grid and restart the configuration process.

## Prompt

You are tasked with creating a **Flask-based web application** that features an interactive grid map where users can run a **value iteration algorithm**. The application requirements are as follows:

1. **Grid Setup:**
   - Allow the user to specify the grid size, with valid values ranging from **5 to 9**.
   - Dynamically generate an **nxn grid** where each cell can be clicked.

2. **User Interactions:**
   - On the first click, mark the selected cell as the **start point** (displayed in **green**).
   - On the second click, mark the selected cell as the **end point** (displayed in **red**).
   - Allow the user to click on additional cells to mark **obstacles** (displayed in **gray**), up to a maximum of **n-2 obstacles**.
   - Include a **status description area** that updates the user on the current selection state (e.g., "Please select the start point", "Please select the end point", "Please select obstacles; X remaining").

3. **Value Iteration Algorithm:**
   - Implement a **value iteration algorithm** in JavaScript to compute the **optimal policy** for each cell.
   - Display both the **optimal action** (using arrows) and the **computed state value** in each non-obstacle cell.
   - Optionally animate the optimal path from the start to the end cell, ensuring that the cell colors are applied completely without partial rendering issues.

4. **UI and Layout Enhancements:**
   - Use **Bootstrap** for styling and responsiveness to adapt to different screen sizes and aspect ratios.
   - Arrange all control buttons (**Create Grid**, **Reset**, **Compute**) in a single row.
   - Remove any unnecessary animation effects (such as hover scaling) that might cause visual glitches; ensure that when a cell is selected, its color fills the entire cell.
   - Provide clear instructions and a **status indicator** so that users always know what selection is required next.

Your final code should include an **HTML template** using **Bootstrap** for styling, embedded **JavaScript** to handle grid interactions and the value iteration computation, and a simple **Flask backend** to render the template. Ensure that the code is **modular, well-documented, and visually appealing**.

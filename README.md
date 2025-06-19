# ✈️ Flight Route Finder – Python Console Application

This is a Python console application that simulates airline route finding between countries. It allows users to display all available flight paths between two countries and determine the shortest-duration route. The application is structured with a main menu, nested dictionaries, and clear user interaction, and was developed as an individual coursework for the **DOC 333 – Introduction to Programming Principles** module.

---

## 📌 Features

- 🌍 Find all possible airline routes between two given countries
- 🕒 Display the least duration route between countries
- ✅ Handles input validation and exit confirmation
- 🧭 Uses a nested dictionary for route and time storage
- 🧪 Includes multiple test cases and validations

---

## 📁 Project Structure
📦 FlightRouteFinder
├── flight_routes.py # Main logic file with menus and functions
├── data/ # (Optional) directory for route data if expanded
└── README.md # This file
---

## ▶️ How to Run

1. Ensure you have Python 3 installed.
2. Download or clone the repository.
3. Open a terminal and navigate to the project folder.
4. Run the program:

```bash
python flight_routes.py
🧠 Core Functionality
🧩 Data Structure
Uses a nested dictionary structure to define routes:
flight_routes = {
    'SRI LANKA': {'JAPAN': 10, 'SINGAPORE': 5, 'AUSTRALIA': 9.25},
    'SINGAPORE': {'JAPAN': 6, 'AUSTRALIA': 7.25, 'USA': 15},
    ...
}

📋 Main Menu Options
FlightRoutes Company - Main Menu

1. Display all possible airline routes between two given countries with durations
2. Display least time airline route between two given countries
3. Exit

🧪 Sample Test Cases
Test Case	Input	Expected Result
1	SL to Australia (Option 1)	Multiple routes with durations
2	Japan to USA (Option 2)	Shortest route and time
3	Invalid country input	User prompt with error message
4	Exit with "Yes"	Program exits with thank you message
5	Exit with "No"	Returns to main menu

📝 Assumptions
Only one-way flights are allowed (no returns)

Inputs are converted to uppercase for consistency

"Yes" (case-insensitive) confirms exit; any other input means "No"

Country names should be typed in full (e.g., SRI LANKA, not SL)

👨‍💻 Developer Info
Name: W.V.V.A. Botheju

Module: DOC 333 – Introduction to Programming Principles

Institute: Informatics Institute of Technology (IIT)

Assignment Type: Individual Coursework

📜 License
This code is submitted for academic purposes. Reuse is allowed for learning only.
If you adapt this work, please credit the original author.

🎓 Developed for the DOC 333 module as part of the Foundation Certificate in Higher Education.

# Student Grade Calculator

## Project Title
**Student Grade Calculator Using Python**

## Overview
Student Grade Calculator is a beginner-level command-line Python project. It asks for a student's name and marks in five subjects—English, Hindi, Maths, Science, and Computer—then calculates the total and percentage and displays a grade and pass/fail result.

## Features
- Accepts the student's name.
- Takes marks for five subjects.
- Calculates total marks out of 500.
- Calculates percentage.
- Applies conditional rules to show a grade and result.
- Prints a simple report card in the terminal.

## Technologies and Tools Used
- **Language:** Python 3
- **Editor:** Visual Studio Code (VS Code)
- **Interface:** Terminal / command prompt
- **Libraries:** No third-party libraries are required for the basic version.

## Installation
1. Install Python 3 from https://www.python.org/downloads/.
2. Install Visual Studio Code from https://code.visualstudio.com/ (or use another text editor).
3. In VS Code, open the folder containing `student_grade_calculator.py`.
4. Make sure the Python interpreter is available in the terminal.

## How to Run
Open VS Code's terminal (**Terminal → New Terminal**) and run:

```bash
python student_grade_calculator.py
```

On some systems, use:

```bash
py student_grade_calculator.py
```

or:

```bash
python3 student_grade_calculator.py
```

Follow the prompts to enter the student's name and marks for each subject.

## Instructions for Testing
Use the following cases to check the program. Compare the actual output with the expected calculations.

| Test | Example input | Expected check |
|---|---|---|
| 1 | 100 in all five subjects | Total 500; percentage 100% |
| 2 | 85, 90, 78, 88, 95 | Total 436; percentage 87.2% |
| 3 | 40 in all five subjects | Total 200; percentage 40% |
| 4 | Any one subject below 33 | Result should be Fail if 33 is the subject pass threshold |
| 5 | 0 in all five subjects | Total 0; percentage 0%; fail under the example rules |

**Important:** The current source code should be checked and corrected before final submission. In particular, verify the grade thresholds, the spelling of the `result` variable, and that the `if/elif/else` block is valid Python. Also test invalid entries and marks outside 0–100 if input validation is added.

## Screenshots (Optional but Recommended)
Add screenshots showing:
1. The program running in the VS Code terminal with sample input.
2. The final report-card output.
3. The project files in VS Code or the GitHub repository.

## Project Structure
```text
student-grade-calculator/
├── student_grade_calculator.py
└── README.md
```

## Conclusion
This project provides practice with Python input/output, variables, type conversion, arithmetic operators, and conditional statements.

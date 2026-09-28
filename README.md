# Medical Report Management System

A Python-based command-line interface (CLI) application designed to record patient details, perform automated physiological calculations, and generate health summaries based on medical indicators.

---

## Overview

The **Medical Report Management System** is an interactive console program developed for introductory problem-solving coursework. It allows healthcare professionals or users to input demographic data, medical history, physical measurements, and blood lab results. The system automatically processes inputs to compute metrics like **Body Mass Index (BMI)** and provides immediate diagnostic feedback—complete with World Health Organization (WHO) classifications, medical suggestions, and precautionary advice for blood pressure, liver markers, cholesterol, and heart rates.

---

## Features

* **Interactive CLI Header:** Displays standard course, student, and registration metadata upon execution.
* **Patient Demographics:** Captures personal details including name, age, gender selection, contact number, and address.
* **BMI Calculation & WHO Classification:** Automatically calculates Body Mass Index ($BMI = \frac{\text{weight}}{\text{height}^2}$) and categorizes the patient under *Underweight*, *Normal Weight*, *Overweight*, or *Obese*.
* **Medical History Tracking:** Records status for active/inactive conditions such as Migraines and Allergies.
* **Cardiovascular Assessment:**
* Evaluates **Systolic & Diastolic Blood Pressure** against standard thresholds and offers lifestyle/prescriptive suggestions.
* Assesses **Pulse Rate** for conditions such as *Bradycardia* ($< 60\text{ bpm}$) and *Tachycardia* ($> 100\text{ bpm}$).
* Evaluates **Total Cholesterol** levels and provides nutritional remedies for high levels.


* **Liver Function Tests (LFT):**
* Measures **SGPT (ALT)** and **SGOT (AST)** levels to flag potential liver issues.
* Assesses **Bilirubin** levels for indicators of *Jaundice*.



---

## Technologies & Tools Used

* **Programming Language:** Python 3.x
* **Standard Libraries:** Native Python I/O modules (`print`, `input`)
* **Development Environment:** Any standard IDE/Text Editor (VS Code, PyCharm, IDLE, or Terminal)

---

## Steps to Install & Run the Project

### Prerequisites

* Ensure **Python 3.x** is installed on your system. You can check your version by running:
```bash
python --version

```


*(or `python3 --version` on macOS/Linux)*

### Installation & Execution

1. **Clone or Download the Repository:**
```bash
git clone https://github.com/your-username/medical-report.git
cd medical-report

```


*(Alternatively, save the provided script as `main.py` or `medical_report.py`).*
2. **Run the Script:**
Open your terminal/command prompt and execute:
```bash
python main.py

```


*(Use `python3 main.py` if running on Linux/macOS).*
3. **Follow the On-Screen Prompts:**
Press `Enter` to bypass the header and enter patient details sequentially.

---

## Instructions for Testing

To verify all conditional branches, run the script multiple times using the sample test cases below:

| Test Case | Height (m) | Weight (kg) | Systolic / Diastolic | Pulse Rate | Total Cholesterol | Expected Outputs |
| --- | --- | --- | --- | --- | --- | --- |
| **Case 1: Normal Range** | `1.75` | `68` | `110` / `70` | `72` | `-1` *(or normal)* | Normal BMI, Normal BP, Normal Pulse |
| **Case 2: Elevated/Risk** | `1.60` | `85` | `135` / `90` | `105` | `220` | Obese BMI, High BP Suggestions, Tachycardia, High Cholesterol Advice |
| **Case 3: Low BP & Pulse** | `1.80` | `52` | `85` / `55` | `50` | `150` | Underweight BMI, Low BP Suggestions, Bradycardia |

---

## Screenshots

*(Optional: Add terminal execution screenshots here)*

```text
+------------------------------------------------------------+
|                      MEDICAL REPORT                        |
+------------------------------------------------------------+
| Name         : Harsh Ranjan                                |
| Register No. : 26BSA10018                                  |
| Course Code  : CSE1021                                     |
| Course Title : Introduction To Problem Solving             |
+------------------------------------------------------------+

Press Enter to continue...
************************************************************

Please Enter Your Name Here: John Doe
Please Enter Your Age: 28
...

```

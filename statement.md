# Problem Statement & System Scope

## Problem Statement
In clinical and primary healthcare settings, manually recording patient vital signs, physiological measurements, and basic laboratory data often leads to errors in initial health assessments. Non-automated evaluation of critical markers—such as Body Mass Index (BMI), Blood Pressure (BP) classifications, pulse rates, and liver enzymes—can delay necessary health suggestions or lead to inconsistent risk categorization. 

There is a need for a lightweight, standardized computational tool that captures key clinical metrics, processes them against established medical benchmarks (such as WHO classification standards), and instantly alerts operators to abnormal parameters along with baseline actionable guidance.

---

## Scope of the Project

### Included in Scope
* **Demographic & Administrative Logging:** Capturing patient personal identification, physician information, and academic/institutional metadata.
* **Automated Physiological Computation:** Calculating Body Mass Index (BMI) using standard mathematical formulas based on metric inputs ($BMI = \frac{\text{weight}}{\text{height}^2}$).
* **Diagnostic Categorization:** Processing physiological and biochemical inputs against predefined threshold conditions, including:
  * WHO BMI classifications (Underweight, Normal Weight, Overweight, Obese).
  * Cardiovascular metrics (Systolic/Diastolic BP classification, Bradycardia/Tachycardia pulse detection).
  * Lipid profile screening (Total Cholesterol levels).
  * Basic Liver Function Test indicators (SGPT/ALT, SGOT/AST, and Bilirubin/Jaundice detection).
* **Clinical Feedback & Suggestions:** Displaying immediate lifestyle recommendations, warning flags, and standard prescriptive guidelines based on detected abnormalities.

### Out of Scope
* Integration with persistent database systems (e.g., SQL/NoSQL databases) or Electronic Health Record (EHR) platforms.
* Advanced statistical risk modelling or AI-based diagnostic predictions.
* Multi-user authentication, role-based access control, or graphical user interface (GUI) elements.

---

## Target Users

1. **Healthcare Workers & Triage Staff:** Paramedics or medical assistants performing preliminary health screenings at clinics or field check-ups.
2. **Medical Students & Academic Evaluators:** Students and instructors evaluating fundamental problem-solving algorithms, conditional logic implementation, and clinical workflows in Python.
3. **General Users / Individuals:** Individuals seeking a quick console-based self-assessment tool for personal health vitals.

---

## High-Level Features

* **Terminal Header & Branding:** Interactive startup header displaying student/course metadata and administrative details.
* **Interactive Data Input Engine:** Guided CLI prompts for entering patient demographics, medical history, physical measurements, and lab results.
* **Automated BMI & WHO Profiler:** Real-time calculation and categorization of patient body mass against official WHO standards.
* **Cardiovascular Risk Assessor:** Comprehensive blood pressure and pulse analysis providing automatic alerts for hypertension, hypotension, bradycardia, and tachycardia.
* **Biochemical Health Evaluator:** Automated flagging for abnormal liver function enzymes (SGPT/SGOT) and elevated bilirubin levels with standard precautionary suggestions.
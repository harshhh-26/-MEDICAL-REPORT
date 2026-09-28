"""
main.py - Entry Point for Medical Report Application
"""
from config import PROJECT_TITLE
from models import PatientDemographics, MedicalHistory, VitalsAndLabs, PatientRecord
from evaluator import HealthEvaluator
from utils import print_header, get_valid_input
from storage import save_patient_record

def main():
    print_header()
    input("Press Enter to begin patient evaluation...")
    print("\n" + "="*60)
    print("PATIENT DEMOGRAPHICS")
    print("="*60)

    name = input("Enter Patient Name: ").strip()
    age = get_valid_input("Enter Age: ", int, min_val=0, max_val=120)

    print("\nSelect Gender:")
    print("  1. Male\n  2. Female\n  3. Other")
    gender_choice = get_valid_input("Choice (1-3): ", int, min_val=1, max_val=3)
    gender_map = {1: "Male", 2: "Female", 3: "Other"}
    gender = gender_map[gender_choice]

    contact = input("Enter Contact Number: ").strip()
    address = input("Enter Address: ").strip()

    demographics = PatientDemographics(name, age, gender, contact, address)

    print("\n" + "="*60)
    print("MEDICAL HISTORY")
    print("="*60)
    migraine_choice = get_valid_input("Migraine Status (1: Active, 2: Inactive): ", int, min_val=1, max_val=2)
    allergy_choice = get_valid_input("Allergy Status (1: Yes, 2: No): ", int, min_val=1, max_val=2)

    history = MedicalHistory(
        migraine_active=(migraine_choice == 1),
        is_allergic=(allergy_choice == 1)
    )

    print("\n" + "="*60)
    print("PHYSICAL & BLOOD LAB MEASUREMENTS")
    print("="*60)
    height = get_valid_input("Height in meters (e.g., 1.75): ", float, min_val=0.5, max_val=2.5)
    weight = get_valid_input("Weight in kg (e.g., 70): ", float, min_val=2.0, max_val=300.0)
    systolic = get_valid_input("Systolic BP (mmHg): ", int, min_val=50, max_val=250)
    diastolic = get_valid_input("Diastolic BP (mmHg): ", int, min_val=30, max_val=150)
    pulse = get_valid_input("Pulse Rate (bpm): ", int, min_val=30, max_val=220)
    cholesterol = get_valid_input("Total Cholesterol (mg/dL): ", float, min_val=50.0, max_val=500.0)
    sgpt = get_valid_input("SGPT/ALT Level (U/L): ", float, min_val=0.0, max_val=500.0)
    sgot = get_valid_input("SGOT/AST Level (U/L): ", float, min_val=0.0, max_val=500.0)
    bilirubin = get_valid_input("Total Bilirubin (mg/dL): ", float, min_val=0.0, max_val=30.0)

    vitals = VitalsAndLabs(height, weight, systolic, diastolic, pulse, cholesterol, sgpt, sgot, bilirubin)
    record = PatientRecord(demographics, history, vitals)

    # Output Diagnostics
    print("\n" + "*"*60)
    print("                      GENERATED MEDICAL REPORT")
    print("*"*60)
    print(f" Patient Name : {demographics.name} | Age: {demographics.age} | Gender: {demographics.gender}")
    print(f" Contact      : {demographics.contact}")
    print("-" * 60)
    
    print(f"\n[1] Physical Metrics:")
    print(f"    - BMI Level    : {vitals.bmi} kg/m²")
    print(f"    - WHO Category : {HealthEvaluator.evaluate_bmi(vitals.bmi)}")

    print(f"\n[2] Cardiovascular Health:")
    bp_eval = HealthEvaluator.evaluate_bp(vitals.systolic_bp, vitals.diastolic_bp)
    print(f"    - Blood Pressure : {vitals.systolic_bp}/{vitals.diastolic_bp} mmHg ({bp_eval['status']})")
    print(f"      Advice         : {bp_eval['suggestions']}")
    print(f"      Medication     : {bp_eval['medicine']}")

    print(f"    - Pulse Evaluation: {HealthEvaluator.evaluate_pulse(vitals.pulse_rate)}")

    chol_eval = HealthEvaluator.evaluate_cholesterol(vitals.cholesterol)
    print(f"    - Cholesterol     : {vitals.cholesterol} mg/dL ({chol_eval['status']})")
    if chol_eval['remedy']:
        print(f"      Remedy Advice   : {chol_eval['remedy']}")

    print(f"\n[3] Liver Function Tests:")
    lft = HealthEvaluator.evaluate_lft(vitals.sgpt, vitals.sgot, vitals.bilirubin)
    print(f"    - SGPT / ALT  : {vitals.sgpt} U/L -> {lft['sgpt']}")
    print(f"    - SGOT / AST  : {vitals.sgot} U/L -> {lft['sgot']}")
    print(f"    - Bilirubin   : {vitals.bilirubin} mg/dL -> {lft['bilirubin']}")

    print("\n" + "="*60)
    print("                     HEALTH IS WEALTH")
    print("="*60)

    save_patient_record(record)

if __name__ == "__main__":
    main()
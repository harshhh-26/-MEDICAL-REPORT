"""
evaluator.py - Diagnostic Engine and Clinical Rules
"""
from config import (
    BMI_THRESHOLDS, BLOOD_PRESSURE, PULSE_RANGES,
    CHOLESTEROL_MAX, LFT_RANGES
)

class HealthEvaluator:

    @staticmethod
    def evaluate_bmi(bmi: float) -> str:
        if bmi < BMI_THRESHOLDS["underweight"]:
            return "Underweight"
        elif bmi < BMI_THRESHOLDS["normal"]:
            return "Normal Weight"
        elif bmi < BMI_THRESHOLDS["overweight"]:
            return "Overweight"
        else:
            return "Obese"

    @staticmethod
    def evaluate_bp(systolic: int, diastolic: int) -> dict:
        if systolic < BLOOD_PRESSURE["sys_low_max"] or diastolic < BLOOD_PRESSURE["dia_low_max"]:
            return {
                "status": "Low Blood Pressure",
                "suggestions": "Maintain adequate fluid intake. Sit or lie down if dizzy.",
                "medicine": "No automatic medication prescribed. Consult physician."
            }
        elif systolic > BLOOD_PRESSURE["sys_normal_max"] or diastolic > BLOOD_PRESSURE["dia_normal_max"]:
            return {
                "status": "High Blood Pressure",
                "suggestions": "Reduce excess sodium, exercise regularly, and avoid smoking.",
                "medicine": "Antihypertensive medication only as prescribed by doctor."
            }
        else:
            return {
                "status": "Normal Blood Pressure",
                "suggestions": "Maintain healthy lifestyle habits.",
                "medicine": "None required."
            }

    @staticmethod
    def evaluate_pulse(pulse: int) -> str:
        if pulse < PULSE_RANGES["bradycardia"]:
            return "Bradycardia (Abnormally low heart rate)"
        elif pulse <= PULSE_RANGES["tachycardia"]:
            return "Normal Pulse Rate"
        else:
            return "Tachycardia (Abnormally high heart rate)"

    @staticmethod
    def evaluate_cholesterol(level: float) -> dict:
        if level <= CHOLESTEROL_MAX:
            return {"status": "Normal Cholesterol Level", "remedy": None}
        else:
            return {
                "status": "High Cholesterol Level",
                "remedy": "Reduce saturated/trans fats, increase fiber-rich foods. Statins may be prescribed by doctor."
            }

    @staticmethod
    def evaluate_lft(sgpt: float, sgot: float, bilirubin: float) -> dict:
        results = {}

        # SGPT
        if LFT_RANGES["sgpt_normal_min"] <= sgpt <= LFT_RANGES["sgpt_normal_max"]:
            results["sgpt"] = "Normal Level"
        else:
            results["sgpt"] = "Elevated - Possible Liver Involvement (Avoid alcohol, consult doctor)"

        # SGOT
        if LFT_RANGES["sgot_normal_min"] <= sgot <= LFT_RANGES["sgot_normal_max"]:
            results["sgot"] = "Normal Level"
        else:
            results["sgot"] = "Elevated - Further Liver Function Tests Recommended"

        # Bilirubin
        if LFT_RANGES["bilirubin_normal_min"] <= bilirubin <= LFT_RANGES["bilirubin_normal_max"]:
            results["bilirubin"] = "Normal Level"
        else:
            results["bilirubin"] = "Elevated - Possible Jaundice Indicator (Requires medical evaluation)"

        return results
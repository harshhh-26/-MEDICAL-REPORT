"""
config.py - System Configuration & Reference Ranges
"""

PROJECT_TITLE = "Medical Report Management System"
AUTHOR = "Harsh Ranjan"
REGISTER_NO = "26BSA10018"
COURSE_CODE = "CSE1021"
COURSE_TITLE = "Introduction To Problem Solving"

# Diagnostic Ranges & Thresholds
BMI_THRESHOLDS = {
    "underweight": 18.5,
    "normal": 25.0,
    "overweight": 30.0,
}

BLOOD_PRESSURE = {
    "sys_normal_max": 120,
    "sys_low_max": 90,
    "dia_normal_max": 80,
    "dia_low_max": 60,
}

PULSE_RANGES = {
    "bradycardia": 60,
    "tachycardia": 100,
}

CHOLESTEROL_MAX = 200.0

LFT_RANGES = {
    "sgpt_normal_min": 4.0,
    "sgpt_normal_max": 36.0,
    "sgot_normal_min": 8.0,
    "sgot_normal_max": 33.0,
    "bilirubin_normal_min": 0.1,
    "bilirubin_normal_max": 1.2,
}
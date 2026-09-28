"""
storage.py - File I/O for Patient Records
"""
import json
import os
from models import PatientRecord

DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "reports.json")

def save_patient_record(record: PatientRecord):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    records = []
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r") as f:
                records = json.load(f)
        except json.JSONDecodeError:
            records = []

    records.append(record.to_dict())

    with open(FILE_PATH, "w") as f:
        json.dump(records, f, indent=4)
    print(f"\n[✓] Record successfully saved to '{FILE_PATH}'")
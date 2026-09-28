"""
models.py - Data Models
"""
from dataclasses import dataclass, asdict

@dataclass
class PatientDemographics:
    name: str
    age: int
    gender: str
    contact: str
    address: str

@dataclass
class MedicalHistory:
    migraine_active: bool
    is_allergic: bool

@dataclass
class VitalsAndLabs:
    height_m: float
    weight_kg: float
    systolic_bp: int
    diastolic_bp: int
    pulse_rate: int
    cholesterol: float
    sgpt: float
    sgot: float
    bilirubin: float

    @property
    def bmi(self) -> float:
        if self.height_m <= 0:
            return 0.0
        return round(self.weight_kg / (self.height_m ** 2), 2)

class PatientRecord:
    def __init__(self, demographics: PatientDemographics, history: MedicalHistory, vitals: VitalsAndLabs):
        self.demographics = demographics
        self.history = history
        self.vitals = vitals

    def to_dict(self) -> dict:
        data = asdict(self)
        data['vitals']['bmi'] = self.vitals.bmi
        return data
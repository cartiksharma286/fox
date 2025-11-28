class Patient:
    def __init__(self, name, age, medical_history):
        self.name = name
        self.age = age
        self.medical_history = medical_history

class Medication:
    def __init__(self, name, dosage, indications):
        self.name = name
        self.dosage = dosage
        self.indications = indications

class PersonalizedMedicine:
    def __init__(self):
        self.patients = []
        self.medications = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_medication(self, medication):
        self.medications.append(medication)

    def recommend_medication(self, patient):
        recommendations = []
        for medication in self.medications:
            if self.is_appropriate(medication, patient):
                recommendations.append(medication)
        return recommendations

    def is_appropriate(self, medication, patient):
        # Placeholder for logic to determine if medication is appropriate
        return True  # Implement actual logic based on patient history

# Example usage
if __name__ == "__main__":
    pm_system = PersonalizedMedicine()
    patient1 = Patient("John Doe", 30, ["hypertension"])
    medication1 = Medication("Lisinopril", "10mg", ["hypertension"])
    
    pm_system.add_patient(patient1)
    pm_system.add_medication(medication1)
    
    recommendations = pm_system.recommend_medication(patient1)
    for med in recommendations:
        print(f"Recommended Medication: {med.name}, Dosage: {med.dosage}")
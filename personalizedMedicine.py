import anthropic

def get_personalized_medicine_recommendation(patient_data: dict) -> str:
    """
    Generate personalized medicine recommendations using Claude AI.
    
    Args:
        patient_data: Dictionary containing patient information
                     (age, symptoms, medical_history, medications, etc.)
    """
    client = anthropic.Anthropic()
    
    prompt = f"""
    Based on the following patient information, provide personalized medicine recommendations:
    
    Patient Data:
    - Age: {patient_data.get('age')}
    - Symptoms: {patient_data.get('symptoms')}
    - Medical History: {patient_data.get('medical_history')}
    - Current Medications: {patient_data.get('medications')}
    - Allergies: {patient_data.get('allergies')}
    
    Please provide:
    1. Potential conditions to investigate
    2. Recommended tests or evaluations
    3. Treatment options
    4. Lifestyle recommendations
    
    Note: This is for informational purposes and not a substitute for professional medical advice.
    """
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text

# Example usage
patient = {
    "age": 45,
    "symptoms": "fatigue, headaches",
    "medical_history": "hypertension",
    "medications": "lisinopril",
    "allergies": "penicillin"
}

recommendation = get_personalized_medicine_recommendation(patient)
print(recommendation)
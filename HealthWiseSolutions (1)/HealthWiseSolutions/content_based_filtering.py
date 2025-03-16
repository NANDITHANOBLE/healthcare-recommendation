"""
Content-Based Filtering module for the Healthcare Recommender System.
This module implements symptom-based treatment suggestions.
"""

# Symptom to treatment database - simulated in-memory database for MVP
# In a real system, this would be a proper database with medical knowledge
symptom_treatment_database = {
    "chest pain": [
        ["Aspirin", "Recommended for suspected heart attack; reduces blood clotting"],
        ["Nitroglycerin", "Relaxes blood vessels, improves blood flow to the heart"],
        ["Oxygen therapy", "Helps provide adequate oxygen to heart tissue"],
        ["Rest", "Reduces heart's workload and oxygen demand"]
    ],
    "high blood pressure": [
        ["Lisinopril", "ACE inhibitor that relaxes blood vessels"],
        ["Amlodipine", "Calcium channel blocker that relaxes blood vessels"],
        ["Low-sodium diet", "Reduces water retention and blood volume"],
        ["Regular exercise", "Helps reduce blood pressure naturally"]
    ],
    "diabetes": [
        ["Metformin", "First-line medication for type 2 diabetes"],
        ["Insulin", "Hormone therapy for type 1 and advanced type 2 diabetes"],
        ["Low-carb diet", "Helps control blood sugar levels"],
        ["Regular blood sugar monitoring", "Essential for diabetes management"]
    ],
    "headache": [
        ["Ibuprofen", "NSAID that reduces inflammation and pain"],
        ["Acetaminophen", "Pain reliever that works on pain receptors"],
        ["Rest", "Reduces sensory stimulation and promotes healing"],
        ["Hydration", "Dehydration is a common headache trigger"]
    ],
    "fever": [
        ["Acetaminophen", "Reduces fever by affecting the hypothalamus"],
        ["Ibuprofen", "Reduces inflammation and fever"],
        ["Hydration", "Prevents dehydration during fever"],
        ["Cool compress", "Helps reduce body temperature externally"]
    ],
    "cough": [
        ["Dextromethorphan", "Cough suppressant for dry coughs"],
        ["Guaifenesin", "Expectorant for productive coughs"],
        ["Honey and lemon", "Natural remedy to soothe throat irritation"],
        ["Humidifier", "Adds moisture to air to reduce cough triggers"]
    ],
    "allergies": [
        ["Cetirizine", "Antihistamine that blocks allergic reactions"],
        ["Nasal saline", "Clears allergens from nasal passages"],
        ["Allergen avoidance", "Reducing exposure to known allergens"],
        ["HEPA filters", "Removes allergens from indoor air"]
    ],
    "back pain": [
        ["Ibuprofen", "Reduces inflammation and pain"],
        ["Physical therapy", "Strengthens muscles and improves posture"],
        ["Heat/cold therapy", "Reduces inflammation and soothes muscles"],
        ["Proper ergonomics", "Prevents strain during daily activities"]
    ],
    "insomnia": [
        ["Melatonin", "Natural sleep hormone supplement"],
        ["Sleep hygiene", "Regular sleep schedule and bedtime routine"],
        ["Limit screen time", "Reduces blue light exposure before bed"],
        ["Relaxation techniques", "Meditation or deep breathing before sleep"]
    ],
    "anxiety": [
        ["Sertraline", "SSRI medication for anxiety disorders"],
        ["Cognitive behavioral therapy", "Psychological treatment for anxiety"],
        ["Deep breathing exercises", "Activates relaxation response"],
        ["Regular physical activity", "Reduces stress hormones"]
    ],
    "depression": [
        ["Fluoxetine", "SSRI medication for depression"],
        ["Psychotherapy", "Talk therapy to address thought patterns"],
        ["Regular exercise", "Increases endorphins and improves mood"],
        ["Social connection", "Reduces isolation and improves wellbeing"]
    ]
}

def recommend_treatments(symptom_desc, top_n=4):
    """
    Recommend treatments based on symptoms using content-based filtering.
    
    Args:
        symptom_desc: Description of symptoms
        top_n: Number of treatments to recommend
        
    Returns:
        list: Recommended treatments with descriptions
    """
    # Clean symptom description
    symptom_desc = symptom_desc.lower().strip()
    
    # Direct match
    if symptom_desc in symptom_treatment_database:
        return symptom_treatment_database[symptom_desc][:top_n]
    
    # Partial match - find most relevant symptoms
    relevant_symptoms = []
    for symptom in symptom_treatment_database:
        if symptom_desc in symptom or any(word in symptom for word in symptom_desc.split()):
            relevant_symptoms.append(symptom)
    
    # If found relevant symptoms, combine their treatments
    if relevant_symptoms:
        all_treatments = []
        for symptom in relevant_symptoms:
            all_treatments.extend(symptom_treatment_database[symptom])
        
        # Return unique treatments (removing duplicates)
        unique_treatments = []
        treatment_names = set()
        for treatment in all_treatments:
            if treatment[0] not in treatment_names:
                unique_treatments.append(treatment)
                treatment_names.add(treatment[0])
                if len(unique_treatments) >= top_n:
                    break
        
        return unique_treatments
    
    # No matches found
    return [["No specific treatment found", "Please consult with a healthcare professional for personalized advice"]]

# For testing
if __name__ == "__main__":
    print(recommend_treatments("chest pain"))
    print(recommend_treatments("headache"))

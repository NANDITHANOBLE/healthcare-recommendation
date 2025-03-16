"""
Hybrid Recommender module for the Healthcare Recommender System.
This module combines collaborative filtering and content-based filtering approaches.
"""

from collaborative_filtering import recommend_patients, patient_database
from content_based_filtering import recommend_treatments

def get_patient_info(patient_id):
    """
    Get patient information for display purposes.
    
    Args:
        patient_id: ID of the patient
        
    Returns:
        dict: Patient information
    """
    if patient_id not in patient_database:
        return {"error": "Patient not found"}
    
    patient_data = patient_database[patient_id]
    return {
        "id": patient_id,
        "age": patient_data[0],
        "gender": patient_data[1],
        "conditions": patient_data[2],
        "current_treatments": patient_data[3]
    }

def get_similar_patients_details(patient_ids):
    """
    Get detailed information about similar patients.
    
    Args:
        patient_ids: List of patient IDs
        
    Returns:
        list: Detailed information about each patient
    """
    return [get_patient_info(pid) for pid in patient_ids]

def hybrid_recommend(patient_id, symptom_desc):
    """
    Generate recommendations using a hybrid approach.
    
    Args:
        patient_id: ID of the patient
        symptom_desc: Description of symptoms
        
    Returns:
        dict: Recommendations from both approaches
    """
    # Get similar patients using collaborative filtering
    similar_patient_ids = recommend_patients(patient_id)
    similar_patients = get_similar_patients_details(similar_patient_ids)
    
    # Get recommended treatments using content-based filtering
    treatments = recommend_treatments(symptom_desc)
    
    # Combine results
    return {
        "patient_info": get_patient_info(patient_id),
        "similar_patients": similar_patients,
        "recommended_treatments": treatments
    }

# For testing
if __name__ == "__main__":
    print(hybrid_recommend(1, "chest pain"))

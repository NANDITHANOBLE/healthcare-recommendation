"""
Collaborative Filtering module for the Healthcare Recommender System.
This module implements patient similarity analysis.
"""

# Patient database - simulated in-memory database for MVP
# In a real system, this would likely be stored in a proper database
patient_database = {
    # patient_id: [age, gender, conditions, treatments]
    1: [45, "M", ["hypertension", "diabetes"], ["lisinopril", "metformin"]],
    2: [52, "F", ["hypertension", "high cholesterol"], ["lisinopril", "simvastatin"]],
    3: [48, "M", ["hypertension", "coronary artery disease"], ["lisinopril", "aspirin"]],
    4: [55, "F", ["diabetes", "high cholesterol"], ["metformin", "atorvastatin"]],
    5: [61, "M", ["diabetes", "hypertension", "heart failure"], ["metformin", "lisinopril", "furosemide"]],
    6: [42, "F", ["asthma"], ["albuterol"]],
    7: [37, "M", ["anxiety"], ["sertraline"]],
    8: [50, "F", ["arthritis"], ["ibuprofen"]],
    9: [67, "M", ["parkinsons"], ["levodopa"]],
    10: [58, "F", ["hypothyroidism"], ["levothyroxine"]]
}

def calculate_similarity(patient_id1, patient_id2):
    """
    Calculate similarity between two patients based on their conditions.
    
    Args:
        patient_id1: ID of the first patient
        patient_id2: ID of the second patient
        
    Returns:
        float: Similarity score (0-1)
    """
    if patient_id1 not in patient_database or patient_id2 not in patient_database:
        return 0
        
    # Extract conditions for both patients
    conditions1 = set(patient_database[patient_id1][2])
    conditions2 = set(patient_database[patient_id2][2])
    
    # Calculate Jaccard similarity
    intersection = len(conditions1.intersection(conditions2))
    union = len(conditions1.union(conditions2))
    
    if union == 0:
        return 0
    
    return intersection / union

def recommend_patients(patient_id, top_n=3):
    """
    Find similar patients based on collaborative filtering.
    
    Args:
        patient_id: ID of the target patient
        top_n: Number of similar patients to return
        
    Returns:
        list: IDs of similar patients sorted by similarity
    """
    # Check if patient exists
    if patient_id not in patient_database:
        return []
    
    # Calculate similarity with all other patients
    similarities = []
    for other_id in patient_database:
        if other_id != patient_id:
            similarity = calculate_similarity(patient_id, other_id)
            similarities.append((other_id, similarity))
    
    # Sort by similarity (descending)
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Return top n similar patients
    return [p_id for p_id, _ in similarities[:top_n]]

# For testing
if __name__ == "__main__":
    print(recommend_patients(1, 3))

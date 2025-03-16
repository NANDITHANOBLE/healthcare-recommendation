import os
import logging
from flask import Flask, render_template, request, jsonify
from hybrid_recommender import hybrid_recommend

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Get current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Create Flask application with explicit folder paths
app = Flask(__name__, 
            template_folder=TEMPLATE_DIR,
            static_folder=STATIC_DIR)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

@app.route('/')
def home():
    """Render the home page with the recommendation form"""
    return render_template("index.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    """Process recommendation requests and return JSON response"""
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input data
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        if 'patient_id' not in data or not data['patient_id']:
            return jsonify({"error": "Patient ID is required"}), 400
            
        if 'symptom_desc' not in data or not data['symptom_desc']:
            return jsonify({"error": "Symptom description is required"}), 400
        
        # Convert and sanitize inputs
        try:
            patient_id = int(data['patient_id'])
            if patient_id <= 0:
                return jsonify({"error": "Patient ID must be a positive number"}), 400
        except ValueError:
            return jsonify({"error": "Patient ID must be a valid number"}), 400
            
        symptom_desc = data['symptom_desc'].lower().strip()
        
        # Get recommendations using hybrid approach
        recommendations = hybrid_recommend(patient_id, symptom_desc)
        
        return jsonify(recommendations)

    except Exception as e:
        logging.error(f"Error processing recommendation: {str(e)}")
        return jsonify({"error": "An unexpected error occurred. Please try again."}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

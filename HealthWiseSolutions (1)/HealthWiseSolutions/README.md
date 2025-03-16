# Healthcare Recommender System

A Flask-based Healthcare Recommender System that provides personalized treatment suggestions using collaborative and content-based filtering approaches.

## Features

- **Patient Similarity Analysis** (Collaborative Filtering)
- **Symptom-Based Treatment Suggestions** (Content-Based Filtering)
- **Hybrid Approach** (Combining both methods)
- **Web Interface** with Flask, HTML, CSS, and JavaScript
- **Interactive User Form** for inputting patient details

## VS Code Setup Instructions

### Prerequisites

- Python 3.8 or newer
- VS Code with Python extension

### Setup Steps

1. **Clone or download this repository to your local machine**

2. **Open the project folder in VS Code**

3. **Create a virtual environment (recommended)**
   ```
   python -m venv venv
   ```

4. **Activate the virtual environment**

   - **Windows:**
     ```
     venv\Scripts\activate
     ```
   
   - **macOS/Linux:**
     ```
     source venv/bin/activate
     ```

5. **Install dependencies**
   ```
   pip install flask gunicorn
   ```

6. **Run the application using the VS Code-compatible script**
   ```
   python run.py
   ```

7. **Access the application**
   - The application will be available at: http://127.0.0.1:5000
   - Your browser should open automatically

## Using the Application

1. Enter a **Patient ID** (1-10)
2. Enter **Symptoms** (e.g., "chest pain", "high blood pressure")
3. Click **Get Recommendations**
4. View personalized recommendations based on:
   - Similar patients with comparable medical conditions
   - Treatments specifically targeting the described symptoms

## Project Structure

```
Healthcare_Recommender/
│── static/                     # Stores CSS and JavaScript files
│   ├── styles.css              # Styling for the frontend
│   ├── script.js               # JavaScript to handle form submission
│── templates/                  # Stores HTML files
│   ├── index.html              # Main frontend page
│── app.py                      # Main Flask application
│── main.py                     # Original entry point
│── run.py                      # VS Code compatible entry point
│── collaborative_filtering.py  # Collaborative Filtering logic
│── content_based_filtering.py  # Content-Based Filtering logic
│── hybrid_recommender.py       # Hybrid Recommendation function
```

## Troubleshooting

If you encounter any issues:

1. **Files not found:** Ensure your directory structure matches the one described above

2. **CSS/JS not loading:** Try accessing the file directly in your browser (e.g., http://127.0.0.1:5000/static/styles.css)

3. **Patient ID errors:** Use a Patient ID between 1 and 10 (these are pre-defined in the system)

4. **No recommendations:** Try common symptoms like "chest pain", "high blood pressure", "diabetes", etc.
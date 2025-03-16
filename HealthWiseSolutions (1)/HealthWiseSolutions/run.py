"""
VS Code compatible starter script for the Healthcare Recommender System
This script makes it easier to run the application in VS Code
"""

import os
import sys
import webbrowser
from app import app

def check_environment():
    """Check if the environment is properly set up"""
    print("Checking environment...")
    required_folders = ['static', 'templates']
    for folder in required_folders:
        if not os.path.isdir(folder):
            print(f"ERROR: {folder} folder not found!")
            return False
    
    required_files = ['static/styles.css', 'static/script.js', 'templates/index.html']
    for file in required_files:
        if not os.path.isfile(file):
            print(f"ERROR: {file} not found!")
            return False
    
    print("Environment check passed!")
    return True

def open_browser(host, port):
    """Open the browser to the application URL"""
    url = f"http://{host}:{port}"
    print(f"Opening browser to {url}")
    webbrowser.open(url)

if __name__ == "__main__":
    if not check_environment():
        print("Environment check failed. Please make sure all files are in place.")
        sys.exit(1)
    
    # Get host and port from environment variables or use defaults
    host = os.environ.get("HOST", "127.0.0.1")  # Default to localhost for VS Code
    port = int(os.environ.get("PORT", 5000))
    
    print(f"Starting Healthcare Recommender System...")
    print(f"Server running at http://{host}:{port}")
    print("Press Ctrl+C to quit")
    
    # Open browser after a short delay to allow the server to start
    if "--no-browser" not in sys.argv:
        # Only attempt to open browser if we're using localhost
        if host in ["127.0.0.1", "localhost"]:
            import threading
            threading.Timer(1.5, open_browser, args=[host, port]).start()
    
    # Start the Flask application
    app.run(host=host, port=port, debug=True)
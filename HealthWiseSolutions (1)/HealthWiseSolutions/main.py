import os
from app import app

if __name__ == "__main__":
    # Get port from environment variable if available, otherwise use 5000
    port = int(os.environ.get("PORT", 5000))
    # In production use 0.0.0.0, for local development you might use 127.0.0.1
    host = os.environ.get("HOST", "0.0.0.0")
    # Start the Flask app
    app.run(host=host, port=port, debug=True)

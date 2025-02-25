from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import sys
import logging
from traceback import format_exc

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Configure logging to print logs in a readable format
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Root route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask app!"})

# Test DB connection route
@app.route('/test-db', methods=['GET'])
def test_db_connection():
    try:
        logging.info("Attempting to connect to the database...")
        # Run a simple query to test the connection
        result = db.engine.execute('SHOW DATABASES;')
        # Fetch one result to ensure the query was successful
        result.fetchone()
        logging.info("Database connection successful")
        return jsonify({"message": "Database connection successful"}), 200
    except Exception as e:
        # Log the full exception traceback
        logging.error(f"Database connection error: {str(e)}\n{format_exc()}")
        return jsonify({"error": f"Database connection error: {str(e)}"}), 500

# Running the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

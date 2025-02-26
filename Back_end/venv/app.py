from flask import Flask,request, jsonify
from flask_cors import CORS
#from flask_sqlalchemy import SQLAlchemy
#from dotenv import load_dotenv
#import os


from sample_questions import Get_questions

# Load environment variables from .env file
#load_dotenv()

app = Flask(__name__)

# Enable CORS for all origins (or specify allowed origins)
CORS(app)

# Database configuration
#app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
#db = SQLAlchemy(app)

# Import the endpoints after configuring app and db
#try:
   # import endpoints
#except Exception as e:
#    print(f"Error importing endpoints: {e}")

# Create database tables within the app context
"""with app.app_context():
    try:
        db.create_all()
        print("Database tables created successfully")
    except Exception as e:
        print(f"Error creating database tables: {e}")"""


@app.route('/', methods=['GET'])
def test():  
    return "Hello"

@app.route('/api/questions', methods=['GET'])
def fetch_questions():
    player_name=request.args['player_name']
    age=int(request.args['age'])
    sub_level=int(request.args['sub_level'])

    print(f"Player_name is {player_name}" )
    questions=Get_questions(player_name,age,sub_level)
    return jsonify(
        {
            "min_score": 3,
            "questions": questions
        }
    ), 200

if __name__ == "__main__":
    app.run(debug=True)



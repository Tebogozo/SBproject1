from flask import request, jsonify
from app import db
from models import User, Score, LevelProgression, Question, Answer
import random

from app import app

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    """Creates a new user."""
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    if not name or not age:
        return jsonify({"error": "Name and age are required."}), 400

    user = User(name=name, age=age)
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_json()), 201


# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    """Fetches all users."""
    users = User.query.all()
    return jsonify([user.to_json() for user in users]), 200


# Endpoint to create a score for a user
@app.route('/scores', methods=['POST'])
def create_score():
    """Creates a new score record for a user."""
    data = request.get_json()
    score = data.get('score')
    badge = data.get('badge')
    correct_streak = data.get('correct_streak')
    total_time = data.get('total_time')
    user_id = data.get('user_id')

    if not score or not user_id:
        return jsonify({"error": "Score and user ID are required."}), 400

    score_record = Score(score=score, badge=badge, correct_streak=correct_streak,
                         total_time=total_time, user_id=user_id)
    db.session.add(score_record)
    db.session.commit()

    return jsonify(score_record.to_json()), 201


# Endpoint to get all scores
@app.route('/scores', methods=['GET'])
def get_scores():
    """Fetches all score records."""
    scores = Score.query.all()
    return jsonify([score.to_json() for score in scores]), 200


# Endpoint to create a question
@app.route('/questions', methods=['POST'])
def create_question():
    """Creates a new question."""
    data = request.get_json()
    question_text = data.get('question_text')
    user_id = data.get('user_id')

    if not question_text or not user_id:
        return jsonify({"error": "Question text and user ID are required."}), 400

    question_id = str(random.randint(100000, 999999))
    question = Question(question_text=question_text, question_id=question_id, user_id=user_id)
    db.session.add(question)
    db.session.commit()

    return jsonify(question.to_json()), 201


# Endpoint to get all questions
@app.route('/questions', methods=['GET'])
def get_questions():
    """Fetches all generated questions."""
    questions = Question.query.all()
    return jsonify([question.to_json() for question in questions]), 200


# Endpoint to post an answer to a question
@app.route('/answers', methods=['POST'])
def create_answer():
    """Creates a new answer for a question."""
    data = request.get_json()
    answer_text = data.get('answer_text')
    user_id = data.get('user_id')
    question_id = data.get('question_id')

    if not answer_text or not user_id or not question_id:
        return jsonify({"error": "Answer text, user ID, and question ID are required."}), 400

    answer = Answer(answer_text=answer_text, user_id=user_id, question_id=question_id)
    db.session.add(answer)
    db.session.commit()

    return jsonify(answer.to_json()), 201


# Endpoint to get all answers for a specific question
@app.route('/answers/<int:question_id>', methods=['GET'])
def get_answers_by_question(question_id):
    """Fetches all answers for a specific question."""
    answers = Answer.query.filter_by(question_id=question_id).all()
    return jsonify([answer.to_json() for answer in answers]), 200


# Endpoint to create a level progression record for a user
@app.route('/level-progressions', methods=['POST'])
def create_level_progression():
    """
    Creates a new level progression record for a user.
    Expects JSON with 'age_level', 'sub_level', and 'user_id' fields.
    
    Returns:
        JSON response containing the level progression details if successful,
        or an error message if validation fails.
    """
    data = request.get_json()
    age_level = data.get('age_level')
    sub_level = data.get('sub_level')
    user_id = data.get('user_id')

    if not age_level or not sub_level or not user_id:
        return jsonify({"error": "Age level, sub level, and user ID are required."}), 400

    level_progression = LevelProgression(age_level=age_level, sub_level=sub_level, user_id=user_id)
    db.session.add(level_progression)
    db.session.commit()

    return jsonify(level_progression.to_json()), 201


# Endpoint to get all level progressions for a user
@app.route('/level-progressions/<int:user_id>', methods=['GET'])
def get_level_progressions(user_id):
    """
    Fetches all level progressions for a user.
    
    Args:
        user_id: The ID of the user for which level progressions are fetched.
    
    Returns:
        JSON response containing a list of all level progressions for the given user.
    """
    level_progressions = LevelProgression.query.filter_by(user_id=user_id).all()
    return jsonify([level_progression.to_json() for level_progression in level_progressions]), 200

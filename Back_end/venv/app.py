from flask import Flask, jsonify, request
from game import get_level_by_age, generate_problem, assign_badge

app = Flask(__name__)

@app.route('/api/level_by_age', methods=['GET'])
def get_level_by_age_api():
    age = request.args.get('age', type=int)
    if age is None:
        return jsonify({'error': 'Age param required.'}), 400
    level = get_level_by_age(age)
    return jsonify({'age': age, 'level': level})

@app.route('/api/generate_problem', methods=['GET'])
def generate_problem_api():
    age_level = request.args.get('age', type=int)
    sub_level = request.args.get('sub_level', type=int)
    if age_level is None or sub_level is None:
        return jsonify({'error': 'Age and Sublevel params are required'}), 400
    question, answer = generate_problem(age_level, sub_level)
    return jsonify({'question': question, 'answer': answer})

@app.route('/api/assign_badge', methods=['GET'])
def assign_badge_api():
    score = request.args.get('score', type=int)
    if score is None:
        return jsonify({'error': 'Score parameter not supplied'}), 400
    badge = assign_badge(score)
    return jsonify({'score': score, 'badge': badge})

if __name__ == "__main__":
    app.run(debug=True)

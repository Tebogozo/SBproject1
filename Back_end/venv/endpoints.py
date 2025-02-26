#from flask import request, jsonify
#from app import db
#from models import User, Score, LevelProgression, Question, Answer
#import random
#from sample_questions import Get_questions

#from app import app

#@app.route('/api/questions', methods=['GET'])
#def fetch_questions():
    #player_name=request.args.get('player_name')
    #age=request.args.get('age')
    #sub_level=request.args.get('sub_level')
    #print(f"Player_name is {player_name}" )
    #questions=Get_questions(player_name,age,sub_level)
    #return jsonify(
        #{
         #   "min_score": 3,
          #  "questions": questions
        #}
    #), 200


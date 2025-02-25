from app import db
import random
import time


class User(db.Model):
    """
    Represents a user in the game.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    age = db.Column(db.SmallInteger, nullable=False)  # Changed to SmallInteger
    
    scores = db.relationship('Score', backref='user', lazy=True)
    level_progressions = db.relationship('LevelProgression', backref='user', lazy=True, cascade="all, delete-orphan")
    questions = db.relationship('Question', backref='user', lazy=True)
    
    def to_json(self):
        """Converts the User instance to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }


class Score(db.Model):
    """
    Stores the score data for each user session.
    """
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    badge = db.Column(db.String(100))
    correct_streak = db.Column(db.Integer, default=0)
    total_time = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def to_json(self):
        """Converts the Score instance to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "score": self.score,
            "badge": self.badge,
            "correct_streak": self.correct_streak,
            "total_time": self.total_time
        }


class LevelProgression(db.Model):
    """
    Stores the progression of a user through different levels and sub-levels.
    """
    id = db.Column(db.Integer, primary_key=True)
    age_level = db.Column(db.Integer, nullable=False)  # Can be validated or restricted to certain ranges
    sub_level = db.Column(db.Integer, nullable=False)  # Can be validated or restricted to certain ranges
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def to_json(self):
        """Converts the LevelProgression instance to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "age_level": self.age_level,
            "sub_level": self.sub_level
        }


class Question(db.Model):
    """
    Stores the generated questions for the game.
    """
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    question_id = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    
    answers = db.relationship('Answer', backref='question', lazy=True)
    
    def to_json(self):
        """Converts the Question instance to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "question_text": self.question_text,
            "question_id": self.question_id,
            "created_at": self.created_at
        }


class Answer(db.Model):
    """
    Stores the answers provided by users for each question.
    """
    id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    
    def to_json(self):
        """Converts the Answer instance to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "answer_text": self.answer_text,
            "user_id": self.user_id,
            "question_id": self.question_id
        }

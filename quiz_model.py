# src/models/quiz_model.py
from sqlalchemy import Column, Integer, String, PickleType
from database import db

class QuizModel(db.Model):
    __tablename__ = 'quizzes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    questions = Column(PickleType, nullable=False)  # Stores a list of questions

    def __init__(self, title, questions):
        self.title = title
        self.questions = questions

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_quiz(cls, quiz_id):
        return cls.query.get(quiz_id)

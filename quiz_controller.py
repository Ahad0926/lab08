# src/controllers/quiz_controller.py
from flask import Blueprint, request, jsonify
from quiz_service import QuizService

quiz_bp = Blueprint('quiz_bp', __name__)

@quiz_bp.route('/api/quizzes', methods=['POST'])
def create_quiz():
    quiz_service = QuizService()
    data = request.json
    quiz_id = quiz_service.create_quiz(data)
    return jsonify({"message": "Quiz created", "quiz_id": quiz_id}), 201

@quiz_bp.route('/api/quizzes/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    quiz_service = QuizService()
    quiz = quiz_service.get_quiz(quiz_id)
    if quiz:
        return jsonify({"title": quiz.title, "questions": quiz.questions}), 200
    else:
        return jsonify({"error": "Quiz not found"}), 404

@quiz_bp.route('/api/quizzes/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    quiz_service = QuizService()
    user_answers = request.json.get("answers")
    score, message = quiz_service.evaluate_quiz(quiz_id, user_answers)
    if score is not None:
        return jsonify({"score": score, "message": message}), 200
    else:
        return jsonify({"error": message}), 404

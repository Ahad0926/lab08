from flask import Blueprint, request, jsonify
from quiz_service import QuizService

quiz_bp = Blueprint('quiz', __name__)
quiz_service = QuizService()


@quiz_bp.route('/api/quizzes', methods=['POST'])
def create_quiz():
    data = request.get_json()
    title = data.get('title')
    questions = data.get('questions')

    if not title or not questions:
        return jsonify({"error": "Title and questions are required."}), 400

    quiz_id = quiz_service.create_quiz(title, questions)
    return jsonify({"message": "Quiz created", "quiz_id": quiz_id}), 201


@quiz_bp.route('/api/quizzes/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    quiz = quiz_service.get_quiz(quiz_id)

    if not quiz:
        return jsonify({"error": "Quiz not found."}), 404

    return jsonify({"id": quiz.id, "title": quiz.title,
                    "questions": quiz.questions}), 200


@quiz_bp.route('/api/quizzes/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    data = request.get_json()
    answers = data.get('answers')

    if not answers:
        return jsonify({"error": "Answers are required."}), 400

    score = quiz_service.evaluate_quiz(quiz_id, answers)

    if score is None:
        return jsonify({"error": "Quiz not found."}), 404

    return jsonify({"message": "Quiz evaluated", "score": score}), 200

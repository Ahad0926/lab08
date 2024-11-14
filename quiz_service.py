# src/services/quiz_service.py
from quiz_model import QuizModel

class QuizService:
    def create_quiz(self, quiz_data):
        title = quiz_data.get("title")
        questions = quiz_data.get("questions")
        new_quiz = QuizModel(title=title, questions=questions)
        new_quiz.save()
        return new_quiz.id

    def get_quiz(self, quiz_id):
        return QuizModel.get_quiz(quiz_id)

    def evaluate_quiz(self, quiz_id, user_answers):
        quiz = self.get_quiz(quiz_id)
        if quiz:
            correct_answers = [q['answer'] for q in quiz.questions]
            score = sum(1 for correct, user in zip(correct_answers, user_answers) if correct == user)
            return score, "Quiz evaluated successfully"
        else:
            return None, "Quiz not found"

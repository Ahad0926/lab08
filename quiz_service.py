from quiz_model import QuizModel


class QuizService:

    @staticmethod
    def create_quiz(title, questions):
        quiz = QuizModel(title=title, questions=questions)
        quiz.save()
        return quiz.id

    @staticmethod
    def get_quiz(quiz_id):
        return QuizModel.get_quiz(quiz_id)

    @staticmethod
    def evaluate_quiz(quiz_id, answers):
        quiz = QuizModel.get_quiz(quiz_id)

        if not quiz:
            return None

        score = 0
        for question, answer in zip(quiz.questions, answers):
            if question['answer'].lower() == answer.lower():
                score += 1

        return score

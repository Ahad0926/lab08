from unittest.mock import patch
from quiz_service import QuizService


@patch.object(QuizService, 'create_quiz')
def test_create_quiz(mock_create_quiz, client):
    mock_create_quiz.return_value = 1

    response = client.post(
        '/api/quizzes',
        json={
            "title": "Sample Quiz",
            "questions": [
                {"text": "Q1?", "answer": "A1"}
            ]
        }
    )

    assert response.status_code == 201
    assert response.json == {"message": "Quiz created", "quiz_id": 1}
    mock_create_quiz.assert_called_once_with(
        "Sample Quiz", [{"text": "Q1?", "answer": "A1"}]
        )


@patch.object(QuizService, 'get_quiz')
def test_get_quiz(mock_get_quiz, client):
    mock_get_quiz.return_value = type(
        'MockQuiz', (object,),
        {"id": 1, "title": "Sample Quiz", "questions": []}
        )

    response = client.get('/api/quizzes/1')

    assert response.status_code == 200
    assert response.json == {"id": 1, "title": "Sample Quiz", "questions": []}
    mock_get_quiz.assert_called_once_with(1)


@patch.object(QuizService, 'evaluate_quiz')
def test_submit_quiz(mock_evaluate_quiz, client):
    mock_evaluate_quiz.return_value = 1

    response = client.post(
        '/api/quizzes/1/submit',
        json={"answers": ["A1"]}
    )

    assert response.status_code == 200
    assert response.json == {"message": "Quiz evaluated", "score": 1}
    mock_evaluate_quiz.assert_called_once_with(1, ["A1"])

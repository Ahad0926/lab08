# tests/test_quiz.py
from unittest.mock import patch, MagicMock
from quiz_service import QuizService

@patch.object(QuizService, 'create_quiz')
def test_create_quiz(mock_create_quiz, client):
    mock_create_quiz.return_value = 1
    response = client.post('/api/quizzes', json={"title": "Sample Quiz", "questions": [{"question": "Q1?", "answer": "A"}]})
    assert response.status_code == 201
    assert response.json == {"message": "Quiz created", "quiz_id": 1}
    mock_create_quiz.assert_called_once_with({"title": "Sample Quiz", "questions": [{"question": "Q1?", "answer": "A"}]})

@patch.object(QuizService, 'get_quiz')
def test_get_quiz(mock_get_quiz, client):
    mock_get_quiz.return_value = MagicMock(title="Sample Quiz", questions=[{"question": "Q1?", "answer": "A"}])
    response = client.get('/api/quizzes/1')
    assert response.status_code == 200
    assert response.json == {"title": "Sample Quiz", "questions": [{"question": "Q1?", "answer": "A"}]}
    mock_get_quiz.assert_called_once_with(1)

@patch.object(QuizService, 'evaluate_quiz')
def test_submit_quiz(mock_evaluate_quiz, client):
    mock_evaluate_quiz.return_value = (1, "Quiz evaluated successfully")
    response = client.post('/api/quizzes/1/submit', json={"answers": ["A"]})
    assert response.status_code == 200
    assert response.json == {"score": 1, "message": "Quiz evaluated successfully"}
    mock_evaluate_quiz.assert_called_once_with(1, ["A"])

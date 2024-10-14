import pytest
from questiontrivia.question import Question

@pytest.fixture
def question():
    return Question(
        description = "Capital of France?",
        options = ["Berlin", "London", "Paris", "Rome"],
        correct_answer = "Paris",
        difficulty = "media"
    )

def test_initialization(question):
    assert question.description == "Capital of France?"
    assert question.options == ["Berlin", "London", "Paris", "Rome"]
    assert question.correct_answer == "Paris"
    assert question.difficulty == "media"

def test_is_correct(question):
    assert question.is_correct("Paris") is True
    assert question.is_correct("Berlin") is False
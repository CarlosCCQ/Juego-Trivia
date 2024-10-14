import pytest
from questiontrivia.question import Question
from questiontrivia.quiz import Quiz

@pytest.fixture
def sample_questions():
    return [
        Question("What is 2 + 2?", ["2", "3", "4", "5"], "4", "fácil"),
        Question("Capital of France?", ["Berlin", "London", "Paris", "Rome"], "Paris", "media"),
        Question("What is the derivative of x^2?", ["2x", "x^2", "x", "0"], "2x", "difícil"),
        Question("What is the Riemann Hypothesis?", 
                    ["A solved problem", "An unsolved problem", "A conjecture about primes", "A proven theorem"], 
                    "A conjecture about primes", "muy difícil")
    ]

def test_initializacion():
    quiz = Quiz()
    assert quiz.current_difficulty == "fácil"
    assert quiz.total_answered_questions == 0
    assert quiz.max_questions == 10
    assert quiz.correct_answer == 0
    assert quiz.incorrect_answer == 0
    assert quiz.answered_questions == {
        "fácil": 0,
        "media": 0,
        "difícil": 0,
        "muy difícil": 0
    }

def test_add_question(sample_questions):
    quiz = Quiz()
    quiz.add_question(sample_questions[0])
    assert len(quiz.questions) == 1
    assert quiz.questions[0].description == "What is 2 + 2?"

def test_get_next_question(sample_questions):
    quiz = Quiz()
    for question in sample_questions:
        quiz.add_question(question)

    question = quiz.get_next_question()
    assert question.description == "What is 2 + 2?"
    assert quiz.total_answered_questions == 1

    question = quiz.get_next_question()
    assert question.description == "Capital of France?"
    assert quiz.total_answered_questions == 2

def test_answer_question_correctly(sample_questions):
    quiz = Quiz()
    for question in sample_questions:
        quiz.add_question(question)

    question = quiz.get_next_question()
    assert quiz.answer_question(question, "4")
    assert quiz.correct_answer == 1
    assert quiz.incorrect_answer == 0

def test_answer_question_incorrectly(sample_questions):
    quiz = Quiz()
    for question in sample_questions:
        quiz.add_question(question)

    question = quiz.get_next_question()
    assert not quiz.answer_question(question, "2")
    assert quiz.correct_answer == 0
    assert quiz.incorrect_answer == 1

def test_difficulty_transition(sample_questions):
    quiz = Quiz()
    for question in sample_questions:
        quiz.add_question(question)

    quiz.get_next_question()
    quiz.answer_question(quiz.questions[0], "4")
    quiz.get_next_question()
    quiz.answer_question(quiz.questions[1], "Paris")

    quiz.get_next_question()
    assert quiz.current_difficulty == "difícil"
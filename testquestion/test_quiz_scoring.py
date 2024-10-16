import pytest

from questiontrivia.question import Question
from questiontrivia.quiz import Quiz 

@pytest.fixture
def setup_quiz():
    quiz = Quiz()

    quiz.add_question(Question("What is 2 + 2?",["1","2","3","4"],"4","fácil"))
    quiz.add_question(Question("What is 5 * 5?",["10","15","25","30"],"25","fácil"))
    quiz.add_question(Question("Capital of France?",["Berlin","London","Paris","Rome"],"Paris","media"))
    quiz.add_question(Question("Square root of 144?",["10","11","12","13"],"12","media"))
    return quiz

def test_correct_answer_increases_score(setup_quiz):
    quiz = setup_quiz
    question = quiz.questions[0]
    quiz.answer_question(question, "4")
    assert quiz.correct_answer == 1
    assert quiz.incorrect_answer == 0

def test_score_after_multiple_questions(setup_quiz):
    quiz = setup_quiz
    for question in quiz.questions:
        if question.description == "What is 2 + 2?":
            quiz.answer_question(question, "4")
        elif question.description == "What is 5 * 5?":
            quiz.answer_question(question, "25")
        elif question.description == "Capital of France?":
            quiz.answer_question(question, "Paris")
        else:
            quiz.answer_question(question, "11")
    
    assert quiz.correct_answer == 3
    assert quiz.incorrect_answer == 1
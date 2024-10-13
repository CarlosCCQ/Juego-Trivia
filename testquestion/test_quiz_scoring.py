import pytest

from questionTrivia.question import Question
from questionTrivia.quiz import Quiz 

"""from questionTrivia.quiz import Quiz
from questionTrivia.question import Question"""

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
        else:
            quiz.answer_question(question, "Berlin")
    
    assert quiz.correct_answer == 3
    assert quiz.incorrect_answer == 1

"""def test_quiz_scoring():
    quiz = Quiz()
    question = Question("What is 2 + 2?",["1","2","3","4"],"4")
    quiz.add_question(question)
    assert quiz.answer_question(question,"4") == True
    assert quiz.correct_answer == 1

def test_quiz_scoring_incorrect_answer():
    quiz = Quiz()
    question = Question("What is 2 + 2?",["1","2","3","4"],"4","fácil")
    quiz.add_question(question)
    assert not quiz.answer_question(question,"2")
    assert quiz.incorrect_answer == 1"""
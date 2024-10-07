import pytest
from questionTrivia.quiz import Quiz
from questionTrivia.question import Question

def test_quiz_scoring():
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
    assert quiz.incorrect_answer == 1
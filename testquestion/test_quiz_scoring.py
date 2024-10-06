import pytest
from question import Quiz, Question

def test_quiz_scoring():
    quiz = Quiz()
    question = Question("What is 2 + 2?",["1","2","3","4"],"4")
    quiz.add_question(question)
    assert quiz.answer_question(question,"4") == True
    assert quiz.correct_answer == 1
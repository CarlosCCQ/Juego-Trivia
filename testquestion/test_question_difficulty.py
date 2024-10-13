import pytest
from questionTrivia.question import Question

def test_question_has_difficulty():
    question = Question("What is 2 + 2?",["1","2","3","4"],"4","fácil")
    assert question.difficulty == "fácil"

def test_question_is_correct():
    question = Question("Whas is 2 + 2?",["1","2","3","4"],"4","fácil")
    assert question.is_correct("4")

def test_question_is_incorrect():
    question = Question("Whas is 2 + 2?",["1","2","3","4"],"4","fácil")
    assert not question.is_correct("2")

def test_question_difficulty_level():
    easy_question = Question("What is 2 + 2?",["1","2","3","4"],"4","fácil")
    medium_question = Question("Capital of France?",["Berlin","London","Paris","Roma"],"Paris","media")
    hard_question = Question("Square root of 144?",["10","11","12","13"],"12","difícil")

    assert easy_question.difficulty == "fácil"
    assert medium_question.difficulty == "media"
    assert hard_question.difficulty == "difícil"
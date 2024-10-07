import pytest
from questionTrivia.quiz import Quiz
from questionTrivia.question import Question

def test_quiz_starts_with_easy_questions():
    quiz = Quiz()
    easy_question = Question("What is 2 + 2?",["1","2","3","4"],"4","fácil")
    quiz.add_question(easy_question)

    question = quiz.get_next_question()
    assert question.description == "What is 2 + 2?"
    assert question.difficulty == "fácil"
def test_quiz_adjusts_to_medium():
    quiz = Quiz()
    easy_question = Question("What 2 + 2?", ["1","2","3","4"],"4","fácil")
    medium_question = Question("Capital de France?",["Berlin","London","Paris","Roma"],"Paris","media")
    
    for _ in range(3):
        quiz.add_question(easy_question)

    quiz.answer_question(quiz.get_next_question(),"4")
    quiz.answer_question(quiz.get_next_question(),"4")

    quiz.add_question(medium_question)
    assert quiz.current_difficulty == "media"

def test_quiz_adjusts_to_hard():
    quiz = Quiz()
    esay_question = Question("What is 2 + 2?",["1","2","3","4"],"4","fácil")
    medium_question = Question("Capital of France?",["Berlin","London","Paris","Roma"],"Paris","media")
    hard_question = Question("Square root of 144",["10","11","12","13"],"12","difícil")

    for _ in range(3):
        quiz.add_question(esay_question)
    for _ in range(3):
        quiz.add_question(medium_question)
    
    quiz.answer_question(quiz.get_next_question(),"4")
    quiz.answer_question(quiz.get_next_question(),"4")
    quiz.answer_question(quiz.get_next_question(),"4")
    quiz.answer_question(quiz.get_next_question(),"Paris")

    quiz.add_question(hard_question)
    assert quiz.current_difficulty == "difícil"

def test_quiz_downgrades_difficulty():
    quiz = Quiz()
    easy_question = Question("What is 2 + 2?",["1","2","3","4"],"4","fácil")
    medium_question = Question("Capital of France?",["Berlin","London","Paris","Roma"],"Paris","media")
    quiz.add_question(easy_question)
    quiz.add_question(medium_question)

    quiz.answer_question(quiz.get_next_question(),"4")
    quiz.answer_question(quiz.get_next_question(),"Paris")
    quiz.answer_question(quiz.get_next_question(),"Wrong answer")
    quiz.answer_question(quiz.get_next_question(),"Wrong answer")
    quiz.answer_question(quiz.get_next_question(),"Wrong answer")

    assert quiz.current_difficulty == "fácil"
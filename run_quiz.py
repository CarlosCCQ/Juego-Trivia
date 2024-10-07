from questionTrivia.question import Question
from questionTrivia.quiz import Quiz

def run_quiz():
    print("Bienvenido al Juego de Trivia!")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta")
    quiz = Quiz()

    quiz.add_question(Question("What is 2 + 2?", ["1", "2", "3", "4"], "4", "fácil"))
    quiz.add_question(Question("What is 5 * 5?", ["10", "15", "25", "30"], "25", "fácil"))
    quiz.add_question(Question("Capital of France?", ["Berlin", "London", "Paris", "Rome"], "Paris", "media"))
    quiz.add_question(Question("Square root of 144?", ["10", "11", "12", "13"], "12", "difícil"))

    while True:
        question = quiz.get_next_question()

        if question:
            print(question.description)
            for idx, option in enumerate(question.options):
                print(f"{idx + 1}) {option}")
            answer = input("Tu respuesta:")
            if quiz.answer_question(question, answer):
                print("¡Correcto!")
            else:
                print("¡Incorrecto!")
            quiz.adjust_difficulty()
        else:
            break
    print("Juego terminado.")
    print(f"Preguntas constestadas: {quiz.current_question_index}")
    print(f"Preguntas correctas: {quiz.correct_answer}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answer}")

if __name__ == "__main__":
    run_quiz()
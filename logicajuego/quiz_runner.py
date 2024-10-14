from questiontrivia.quiz import Quiz
from conexciondatabase.connectdb import connect_db, create_tables, fetch_questions, insert_question
from questiontrivia.question import Question

def run_quiz():
    print("Bienvenido al Juego de Trivia!")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta")
    quiz = Quiz()

    conn = connect_db()
    create_tables(conn)
    questions = fetch_questions(conn)

    if not questions:
        initial_questions = [
            Question("What is 2 + 2?", ["1", "2", "3", "4"], "4", "fácil"),
            Question("What is 5 * 5?", ["10", "15", "25", "30"], "25", "fácil"),
            Question("Capital of Spain?", ["Madrid", "Barcelona", "Valencia", "Sevilla"], "Madrid", "fácil"),
            Question("Which animal is known as the king of the jungle?", ["Lion", "Tiger", "Elephant", "Bear"], "Lion", "fácil"),

            Question("Capital of France?", ["Berlin", "London", "Paris", "Rome"], "Paris", "media"),
            Question("Square root of 144?", ["10", "11", "12", "13"], "12", "media"),
            Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], "Mars", "media"),

            Question("What is the derivative of x^2?", ["2x", "x^2", "x", "0"], "2x", "difícil"),
            Question("What is the integral of 1/x?", ["ln(x)", "x", "1/x^2", "0"], "ln(x) + C", "difícil"),

            Question("What is the Riemann Hypothesis?", 
                    ["A solved problem", "An unsolved problem", "A conjecture about primes", "A proven theorem"], 
                    "A conjecture about primes", "muy difícil")
        ]
        for question in initial_questions:
            insert_question(conn, question)

        questions = fetch_questions(conn)

    for question in questions:
        quiz.add_question(question)

    while True:
        question = quiz.get_next_question()
        if question:
            print(question.description)
            for idx, option in enumerate(question.options):
                print(f"{idx + 1}) {option}")
            answer = input("Tu respuesta: ")
            try:
                selected_index = int(answer) - 1
                if 0 <= selected_index < len(question.options):
                    selected_answer = question.options[selected_index]
                    if quiz.answer_question(question, selected_answer):
                        print("¡Correcto!")
                    else:
                        print("¡Incorrecto!")
            except ValueError:
                print("Opción no válida.")
        else:
            break

    print("Juego terminado.")
    print(f"Preguntas contestadas: {quiz.total_answered_questions}")
    print(f"Preguntas correctas: {quiz.correct_answer}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answer}")

    conn.close()
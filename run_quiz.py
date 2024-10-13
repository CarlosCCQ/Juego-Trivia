import psycopg2
from questionTrivia.quiz import Quiz
from questionTrivia.question import Question

def connect_db():
    conn = psycopg2.connect(
        dbname="trivia_db",
        user="postgres",
        password="carlos123",
        host="localhost",
        port="5432"
    )
    return conn

def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id SERIAL PRIMARY KEY,
            description TEXT NOT NULL,
            options TEXT[] NOT NULL,
            correct_answer TEXT NOT NULL,
            difficulty VARCHAR(50) NOT NULL
        )
        """)
        conn.commit()

def insert_question(conn, question):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO questions (description, options, correct_answer, difficulty) 
        VALUES (%s, %s, %s, %s)
        """, (question.description, question.options, question.correct_answer, question.difficulty))
        conn.commit()

def fetch_questions(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT description, options, correct_answer, difficulty FROM questions")
        rows = cur.fetchall()
        return [Question(row[0], row[1], row[2], row[3]) for row in rows]

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

if __name__ == "__main__":
    run_quiz()
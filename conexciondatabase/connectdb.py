import psycopg2
from questiontrivia.question import Question

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
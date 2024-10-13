from questionTrivia.question import Question

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_difficulty = "fácil"
        self.total_answered_questions = 0
        self.max_questions = 10
        self.correct_answer = 0
        self.incorrect_answer = 0
        
        self.answered_questions = {
            "fácil": 0,
            "media": 0,
            "difícil": 0,
            "muy difícil": 0
        }


    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.total_answered_questions >= self.max_questions:
            return None

        filtered_questions = [q for q in self.questions if q.difficulty == self.current_difficulty]

        if self.answered_questions[self.current_difficulty] >= len(filtered_questions):
            if self.current_difficulty == "fácil":
                self.current_difficulty = "media"
            elif self.current_difficulty == "media":
                self.current_difficulty = "difícil"
            elif self.current_difficulty == "difícil":
                self.current_difficulty = "muy difícil"
            else:
                return None
            
            return self.get_next_question()

        question = filtered_questions[self.answered_questions[self.current_difficulty]]
        self.answered_questions[self.current_difficulty] += 1
        self.total_answered_questions += 1

        return question


    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answer += 1
            return True
        else:
            self.incorrect_answer += 1
            return False

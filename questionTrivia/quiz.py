class Quiz:
    def __init__(self):
        self.questions = {
            "fácil": [],
            "media": [],
            "difícil": []
        }
        self.current_question_index = 0
        self.correct_answer = 0
        self.incorrect_answer = 0
        self.current_difficulty = "fácil"
    
    def add_question(self, question):
        self.questions[question.difficulty].append(question)
    
    def get_next_question(self):
        difficulty_questions = self.questions[self.current_difficulty]
        if self.current_question_index < len(difficulty_questions):
            question = difficulty_questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    
    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answer += 1
            return True
        else:
            self.incorrect_answer += 1
            return False
        
    def adjust_difficulty(self):
        if self.correct_answer >= 2:
            self.current_difficulty = "media"
        if self.correct_answer >= 4:
            self.current_difficulty = "difícil"
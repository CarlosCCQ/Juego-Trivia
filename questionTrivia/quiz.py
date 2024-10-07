class Quiz:
    def __init__(self):
        self.questions = {
            "fácil":[],
            "media":[],
            "difícil":[]
        }
        self.questions = []
        self.current_question_index = 0
        self.correct_answer = 0
        self.incorrect_answer = 0
        self.current_difficulty = "fácil"
    
    def add_question(self, question):
        if question.difficulty in self.questions:
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
            self.adjust_difficulty(True)
            return True
        else:
            self.incorrect_answer += 1
            self.adjust_difficulty(False)
            return False
        
    def adjust_difficulty(self, correct):
        if correct and self.correct_answer % 3 == 0 and self.current_difficulty == "facil":
            self.current_difficulty = "media"
            self.current_question_index = 0
        elif correct and self.correct_answer % 3 == 0 and self.current_difficulty == "media":
            self.current_difficulty = "difícil"
            self.current_question_index = 0
        elif not correct and self.incorrect_answer % 3 == 0 and self.current_difficulty == "media":
            self.current_difficulty = "fácil"
            self.current_question_index = 0
        elif not correct and self.incorrect_answer % 3 == 0 and self.current_difficulty == "difícil":
            self.current_difficulty = "media"
            self.current_question_index = 0
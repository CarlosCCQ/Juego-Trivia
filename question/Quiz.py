class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answer = 0
        self.incorrect_answer = 0
    
    def add_question(self, question):
        self.questions.append(question)
    
    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
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
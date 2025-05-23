class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
        
        self.check_answer(answer, current_question.answer)
        self.question_number += 1
        
        
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")
            
        print(f"Your current score is: {self.score}/{self.question_number + 1}. \n")
            
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
        
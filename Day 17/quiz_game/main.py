from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#Convierto los datos de la lista de diccionarios a una lista de objetos Question
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_questions():
    quiz.next_question()
    
print(f"You've completed the quiz! Your final score was: {quiz.score}/{quiz.question_number}.")
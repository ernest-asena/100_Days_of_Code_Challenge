from question_class import Question
from question_data import question_data
from quizbrain import QuizBrain
question_bank = []
for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('CONGRATULATIONS. You have completed the Challenge!')
print(f"You scored {quiz.score}/{quiz.question_number}.")

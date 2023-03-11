class QuizBrain:
    """This class is responsible for keeping track of the score and the question number."""
    def __init__(self, q_list):
        """Initializes the question number and the score."""
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        """Returns True if there are still questions left in the list, False if not."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Displays the next question and checks if the answer is correct."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"Q.{self.question_number}: {current_question.text}.\nTRUE/FALSE: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks if the answer is correct and displays the result."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print('That was wrong.')
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print('\n')



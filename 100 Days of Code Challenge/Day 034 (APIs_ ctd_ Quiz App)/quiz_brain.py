import html


class QuizBrain:
    """This class is responsible for keeping track of the score and the question number."""
    def __init__(self, q_list):
        """Initialize the class attributes."""
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Check if there are still questions left in the quiz."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Get the next question from the list of questions."""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """Check if the user's answer is correct."""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False


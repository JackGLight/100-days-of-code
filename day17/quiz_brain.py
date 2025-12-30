class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question_number = self.question_number
        current_question = self.question_list[current_question_number]
        current_answer = current_question.answer
        current_text = current_question.text

        while current_question_number < len(self.question_list):
            print(f"Score: {self.score}")
            # print(
            #     # f"The answer is: {self.question_list[current_question_number].answer}"
            # )
            # print(type(self.question_list[current_question_number].answer))

            user_answer = input(
                f"Q.{int(current_question_number)+ 1}: {current_text} (True/False): "
            ).title()

            if user_answer == current_answer:
                print("Correct!")
                self.score += 1
            else:
                print("Wrong!")

            current_question_number += 1
            if current_question_number < len(self.question_list):
                current_question = self.question_list[current_question_number]
                current_answer = current_question.answer
                current_text = current_question.text

        print("You answered all the questions!")
        print(f"Final score: {self.score}")

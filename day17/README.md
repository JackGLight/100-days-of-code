Day 17 – True/False Quiz Game (OOP)

A command-line True/False quiz game built using object-oriented programming.
Questions are stored as structured data, converted into Question objects, and
run through a QuizBrain controller that manages quiz flow and scoring.

Concepts practiced:
- object-oriented programming (classes and objects)
- separating data from application logic
- working with lists of objects
- program flow control with loops
- user input handling and score tracking
- basic project structure across multiple files/modules

Project structure:
- data.py
  - contains `question_data`, a list of question dictionaries (text + answer)
- question_model.py
  - defines the `Question` class used to store question text and correct answer
- quiz_brain.py
  - defines the `QuizBrain` class which runs the quiz, prompts the user, and
    tracks score
- main.py
  - builds the question bank and starts the quiz

How it works:
1. The program loads `question_data` from `data.py`
2. Each question is converted into a `Question` object and stored in a list
3. `QuizBrain` iterates through the question list, prompting the user for
   True/False answers and updating the score
4. The final score is printed at the end of the quiz

How to run:
python main.py
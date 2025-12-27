Day 12 – Number Guessing Game

A command-line number guessing game where the player attempts to guess a randomly
generated number between 1 and 100 within a limited number of attempts.

The game includes selectable difficulty levels, input validation, and feedback
to guide the player toward the correct answer.

Concepts practiced:
- random number generation
- conditional logic
- loops and game flow control
- functions and return values
- input validation and error handling
- state tracking across iterations

How the game works:
- A secret number between 1 and 100 is generated
- The player selects a difficulty level:
  - Easy: 10 attempts
  - Hard: 5 attempts
- After each guess, the player is told whether the guess is too high or too low
- The game ends when the number is guessed correctly or the player runs out of lives

How to run:
python main.py
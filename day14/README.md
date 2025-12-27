Day 14 – Higher Lower Game

A command-line implementation of the Higher Lower guessing game, where players
compare two public figures and guess which one has more social media followers.

The game uses an external dataset, randomly selects comparison pairs, tracks the
player’s score across rounds, and ends when an incorrect guess is made.

Concepts practiced:
- importing data from external Python modules
- working with dictionaries and lists
- random selection
- conditional logic
- game loops and state management
- user input validation

How the game works:
- Two entities (A and B) are presented with descriptions
- The player guesses which has more followers
- Correct guesses increase the score and advance the game
- The higher-followed entity carries over to the next round
- The game ends when the player guesses incorrectly

How to run:
python main.py
'''
Day 12: number guessing game 
'''

import random 




"""initialize lives and set secret num"""
lives = 5
secret_num = random.randint(1, 100)


"""remove life when called"""
def remove_life(life):
    lives_remaining = life
    lives_remaining -= 1
    return lives_remaining


"""check guess and give feedback if guess was valid numeric"""
def check_guess(userInput, secret_num):
    while True:
        try:
            userInput = float(userInput)       
        except ValueError:
            print("Guess again\n")
            break
        else:
            if userInput == secret_num:
                print("You win!")
                exit()
            elif userInput < secret_num:
                print("Too low\n")
            else:
                print("Too high\n")
            break 


"""Game flow"""


print("Welcome to the number guessing game!")
print("I am thinking of a number between 1-100")

difficulty = input("Would you like to play on 'easy' or 'hard' mode?\n").lower()
if difficulty == "easy":
    lives = 10

while lives > 0:
    print(f"You have {lives} lives remaining to guess the number")
    guess = input("what is your guess?:\n")
    check_guess(guess, secret_num)
    lives = remove_life(lives)

print("Out of lives... you lose!")

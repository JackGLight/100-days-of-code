'''
Day 7 of 100 days of code. Hangman game
'''

import random
import os
import string


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']





letters_from_py = list(string.ascii_lowercase)

"""Get options of words based on words.txt file and choose word as random choice"""
BASE_DIR = os.path.dirname(__file__)
words_path = os.path.join(BASE_DIR, "words.txt")

with open(words_path) as file:
    word_list = file.read().splitlines()

# print(word_list)
secret_word = random.choice(word_list)

# secret_word = "tomato"
blanks = ""
letters_guessed = []
lives = 6

# print(len(secret_word))

"""call this function if a new correct letter has been guessed"""
def update_guess_string(blank_string, lg, secret):
    blank_string = "" 
    for char in secret:
        if char in lg:
            blank_string = blank_string + char
        else:
            blank_string = blank_string + "_"
    return blank_string


"""player guess
scenario 1: 
letter has already been guessed
lives do not go down and player needs to guess again

Scenario 2:
new correct letter is guessed
add it to letters guessed list 
update guess string 

scenario 3:
new incorrect letter is guessed 
lives go down 
hangman drawining is updated - might handle with dictionary 


"""

"""call this function if a new letter has been guessed"""
def update_letters_guessed(letter_list, guess):
    letter_list.append(guess)
    letter_list.sort()
    return letter_list


print("Welcome to Hangman!")

blanks = update_guess_string(blanks, letters_guessed, secret_word)


while lives > 0:

    print("****************************************************************")
    print(HANGMANPICS[6 - lives])
    print(f"The word is: {blanks}")
    print(f"Letters guessed: {letters_guessed}")
    print(f"{lives} live(s) left")

    # print(secret_word == blanks)

    current_guess = input("Please guess a letter:").lower()

    #already guessed 
    if current_guess in letters_guessed:
        print("You already guessed that letter!\n")

    #guess is not a valid letter
    elif not current_guess in letters_from_py:
        print("Invalid guess!\n")

    #guess is a new correct guess
    elif current_guess in secret_word:
        print("Good guess!\n")

        #add it to letters guessed
        letters_guessed = update_letters_guessed(letters_guessed, current_guess)

        #update blank 
        blanks = update_guess_string(blanks, letters_guessed, secret_word)

        #check if player won
        if secret_word == blanks:
            print(HANGMANPICS[6 - lives])
            print(f"You win!!! The word was {secret_word}")
            break

    else:
        print(f"{current_guess} is not in the word! :(")
        lives -= 1
        letters_guessed = update_letters_guessed(letters_guessed, current_guess)

        if lives == 0:
            print("You Lose!")
            print(HANGMANPICS[6 - lives])
            break 



    #guess is a new incorrect guess 
    #add it to letters guessed 
    #check if player is out of lives 


    # letters_guessed.append(input("guess a letter"))
    # blanks = update_guess_string(blanks, letters_guessed, secret_word)
    # print(blanks)


'''
Rock Paper Scissors game between computer

Practices using lists, randomization, user input, ASCII graphics
'''

import random

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# print(rock, paper, scissors)


'''
0 for rock
1 for paper
2 for scissors 
'''

def print_graphics(choice):
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)


def computer_move():
    move = random.randint(0, 2)
    return move


def determine_winner(player_move, comp_move):
    if player_move == comp_move:
        return "It's a tie!"
    elif player_move == 0 and comp_move == 2:
        return "You win!"
    elif player_move == 1 and comp_move == 0:
        return "You win!"
    elif player_move == 2 and comp_move == 1:
        return "You win!"
    else:
        return "The computer wins!"
    
    
choices = [0, 1 ,2]
options = ["Rock", "Paper", "Scissors"]
combined = [choices, options]



player_choice = int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissors:\n"))

if player_choice not in (0, 1, 2):
    print("invalid input. You lose!")
else:
    print_graphics(player_choice)
    print(f"You chose {combined[1][player_choice]}\n")

    comp_choice = computer_move()
    print_graphics(comp_choice)
    print(f"The computer chose {combined[1][comp_choice]}")

    print(determine_winner(player_choice, comp_choice))





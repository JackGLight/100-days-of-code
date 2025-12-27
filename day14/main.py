'''
Day 14: Higher Lower game 
'''


import random 
from game_data import data



def a_value():
    a = random.choice(data)
    return a


def b_value(a):
    try:
        b = random.choice(data)
    except a == b:
        b = random.choice(data)
    return b


def check_guess(a, b, guess):
    if not guess == "b" and not guess == "a":
        return "Incorrect"
    elif a > b and guess == "b":
        return "Incorrect"
    elif b > a and guess == "a":
        return "Incorrect"
    else:
        return "Correct"



review = ""
score = 0
a = a_value()
b = b_value(a)


print("Welcome to the higher lower game!")

while True:


    print(f"Current score: {score}")
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
    print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}")

    print(a["follower_count"])
    print(b["follower_count"])

    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    review = check_guess(a["follower_count"],b["follower_count"], guess)

    if review == "Incorrect":
        print("Incorrect!")
        print(f"Game over! Final score: {score}")
        exit()
    else:
        print("Correct!")
        score +=1
        if b["follower_count"] > a["follower_count"]:
            a = b
        b = b_value(a)



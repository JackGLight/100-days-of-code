"""
Day 3: Treasure Island Choose your own adventure 

Uses Conditional statements to allow user to go through choose your own adventure style story
"""

print("""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \*'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\*||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\*/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'      
      
      
      """)

lifestate = 1
score = 0
name = input("Welcome to Treasure Island!\nWhat is your name?")

choice_1 = input(f"Hi {name}!\nYour mission is to find the treasure.\nYou are at a fork in the road,\nwill you take the left path or right path forward?\n").lower()

if not choice_1 == "left":
    print("You have fallen into a hole. Game Over!")
    lifestate = 0

if lifestate == 1:
    score +=1
    choice_2 = input("Good job.\nYou survived the first choice and have arrived at a river.\nWill you attempt to swim across or wait?\n").lower()
    if not choice_2 == "wait":
        print("You have been attacked by trout.\nGame over!")
        lifestate = 0

if lifestate == 1:
    score+=1
    choice_3 = input("""Good job! You waited and a magical bridge rose up from the river allowing you to cross.
You arrive at a cave with three doors. Will you take the red door, blue door, or yellow door?
Please choose R, B, or Y?:\n""").lower()
    
    if choice_3 == "y":
        score+=1
        print("Congratulations - you found the treasure! You win!!!")
    elif choice_3 == "r":
        print("You go through the red door and become trapped as flames engulf you. Game over!")
    elif choice_3 == "b":
        print("You go through the blue door and become trapped as beasts surround and eat you. Game over!")
    else:
        print("Game over! Invalid input >:( ")

print(f"Thanks for playing {name}!\nYour final score was: {score}")
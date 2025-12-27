'''
Day 11: Blackjack
'''

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card(hand):
    hand.append(random.choice(cards))
    return hand

def check_11(hand):
    temp = hand.copy()
    while sum(temp) > 21 and 11 in temp:
        temp[temp.index(11)] = 1
    return temp

def play_blackjack():
    player_hand = []
    dealer_hand = []

    print("\nWelcome to blackjack!")

    # initial deal
    player_hand = check_11(draw_card(draw_card(player_hand)))
    dealer_hand = draw_card(draw_card(dealer_hand))

    print(f"Your cards: {player_hand} (total: {sum(player_hand)})")
    print(f"Computer's first card: {dealer_hand[0]}")

    # player turn
    while True:
        pick_new_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if pick_new_card == "y":
            player_hand = check_11(draw_card(player_hand))
            print(f"Your cards: {player_hand} (total: {sum(player_hand)})")

            if sum(player_hand) > 21:
                print("Bust — you lose!")
                return  # end this round

        elif pick_new_card == "n":
            break

        else:
            print("Invalid input. Please type 'y' or 'n'.")

    # dealer turn
    dealer_hand = check_11(dealer_hand)
    while sum(dealer_hand) < 17:
        dealer_hand = check_11(draw_card(dealer_hand))

    print(f"Computer's cards: {dealer_hand} (total: {sum(dealer_hand)})")

    # decide winner
    if sum(dealer_hand) > 21:
        print("Dealer bust — you win!")
        return

    player_total = sum(player_hand)
    dealer_total = sum(dealer_hand)

    if player_total > dealer_total:
        print("You win!")
    elif dealer_total > player_total:
        print("Computer wins!")
    else:
        print("Tie game!")

# ---- play again loop ----
while True:
    play_blackjack()
    again = input("\nPlay again? Type 'y' or 'n': ").lower()
    if again != "y":
        print("Goodbye!")
        break







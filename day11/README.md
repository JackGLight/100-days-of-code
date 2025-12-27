Day 11 – Blackjack Game

A command-line implementation of the classic Blackjack card game, where a player
competes against a computer-controlled dealer following standard Blackjack rules.

The game supports multiple rounds in a single session, handles Ace values
dynamically (1 or 11), and enforces dealer behavior according to casino rules.

Concepts practiced:
- functions and game flow control
- lists and random selection
- conditional logic and loops
- state management across rounds
- input validation
- basic game rules and simulations

Game rules implemented:
- Player and dealer are each dealt two cards
- Player may hit or stand
- Dealer draws cards until reaching at least 17
- Aces are automatically adjusted from 11 to 1 if the hand would otherwise bust
- Busts and ties are handled appropriately
- Players may choose to play multiple rounds

How to run:
python main.py
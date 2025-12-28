Day 15 – Coffee Machine Simulation

A command-line simulation of a coffee machine that allows users to order drinks,
process payments, manage resources, and dispense change.

The program models a real-world coffee machine by tracking available ingredients,
handling coin-based payments, checking resource sufficiency, and updating machine
state after each transaction.

Concepts practiced:
- nested dictionaries for structured data
- looping and control flow
- functions and return values
- state management across transactions
- resource validation
- arithmetic and rounding logic
- simulating real-world systems

Features:
- Supports espresso, latte, and cappuccino orders
- Checks ingredient availability before processing orders
- Accepts coin-based payments and calculates total value
- Returns change using available coins in the machine
- Updates ingredient and coin resources after each purchase
- Includes administrative commands:
  - `report` to display current resources and money
  - `off` to shut down the machine

How it works:
- Users select a drink or administrative command
- The machine verifies sufficient ingredients
- Users insert coins to pay for the drink
- Change is calculated and returned if necessary
- Ingredients are deducted and the drink is dispensed

How to run:
python main.py
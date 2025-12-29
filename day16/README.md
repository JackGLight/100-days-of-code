Day 16 – Coffee Machine (Object-Oriented Programming)

A command-line coffee machine simulation implemented using object-oriented
programming principles.

This project focuses on interacting with pre-built classes to manage menu items,
resources, and payments, emphasizing composition and object collaboration rather
than procedural logic.

Concepts practiced:
- object-oriented programming (OOP)
- working with classes and objects
- method calls and object interaction
- encapsulation and abstraction
- program orchestration using existing APIs

How it works:
- The program initializes three core objects:
  - `Menu` to manage available drinks
  - `CoffeeMaker` to manage resources and brewing
  - `MoneyMachine` to handle payments
- Users select drinks, request reports, or shut down the machine
- The system checks resource availability and processes payments before brewing
- Internal logic is handled by the provided classes, while `main.py` coordinates flow

Commands:
- espresso / latte / cappuccino — order a drink
- report — display current resources and money
- off — shut down the machine

How to run:
python main.py
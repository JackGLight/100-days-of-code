 # Day 19 — Turtle Racing Simulator

A simple racing game built with Python’s `turtle` module.  
Six turtles race across the screen at random speeds, and the user predicts which color will win.

---

## How It Works

- Six turtles are created, each with a unique color
- Turtles start at the same x-position but different y-positions
- Each turtle moves forward by a random amount each frame
- The first turtle to cross the finish line wins
- The user is prompted to guess the winning turtle before the race starts

---

## Controls & Interaction

- On launch, enter a color when prompted: red, orange, yellow, green, blue, or purple

- The race begins automatically after input
- The result is printed in the console

---

## Requirements

- Python 3.x
- No external dependencies (uses built-in `turtle` and `random` modules)

---

## Run the Program

From the `day19` directory:

```bash
python main.py
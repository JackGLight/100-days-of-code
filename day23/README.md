# Day 23 — Frogger-Style Crossing game

A Frogger-inspired arcade game built with Python’s `turtle` module.  
The player controls a turtle attempting to cross a busy road while avoiding moving cars that increase in speed each level.

---

## Gameplay

- The player starts at the bottom of the screen
- Cars spawn at random lanes and move horizontally across the screen
- The goal is to reach the top safely
- Each successful crossing increases the level and car speed
- The game ends if the turtle collides with a car

---

## Controls

| Key | Action |
|---|---|
| **W** | Move up |
| **S** | Move down |

---

## Features

- Object-oriented design with separate classes for:
  - Player
  - Car manager
  - Scoreboard
- Randomized car generation and colors
- Increasing difficulty with level progression
- Collision detection with moving obstacles
- Safe zones at the top and bottom of the screen
- On-screen level tracking
- Game over screen on collision

---

## Requirements

- Python 3.x
- No external dependencies  
  (uses built-in `turtle`, `time`, and `random` modules)

---

## Run the Game

From the project directory:

```bash
python main.py
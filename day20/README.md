# Day 20 — Snake Game (Part 1) 

A classic Snake game built with Python’s `turtle` module.  
This first part focuses on creating the snake, handling movement, and implementing keyboard controls.

---

## Features Implemented

- Snake composed of multiple square segments
- Initial snake creation using predefined starting positions
- Smooth, continuous movement
- Arrow-key controls (Up, Down, Left, Right)
- Direction-locking logic to prevent reversing into itself

---

## Controls

| Key | Action |
|----|-------|
| ↑ Up Arrow | Move up |
| ↓ Down Arrow | Move down |
| ← Left Arrow | Move left |
| → Right Arrow | Move right |

---

## How It Works

- The snake is represented as a list of `turtle.Turtle` segments
- Each movement step:
  - Segments follow the position of the segment ahead of them
  - The head moves forward by a fixed distance
- Direction changes are restricted to prevent 180° turns

---

## Requirements

- Python 3.x
- Uses only standard library modules:
  - `turtle`
  - `time`

No external dependencies required.

---

## Run the Game

From the `day20` directory:

```bash
python main.py
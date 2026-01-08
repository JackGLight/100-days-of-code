# Day 22 — Pong

A classic Pong clone built with Python’s `turtle` module. Two players control paddles and try to score by getting the ball past the opponent. The ball bounces off walls and paddles and speeds up after paddle hits.

---

## Features

- Two-player paddle controls
- Ball movement with x/y momentum (bounces realistically)
- Wall collision (top and bottom)
- Paddle collision (ball reverses direction + increases speed)
- Score tracking for each player
- Center dashed line for the classic Pong look
- Ball resets to center after a point is scored

---

## Controls

### Right Paddle
- **Up Arrow**: move up  
- **Down Arrow**: move down  

### Left Paddle
- **W**: move up  
- **S**: move down  

---

## Requirements

- Python 3.x  
- No external dependencies (uses built-in `turtle` and `time`)

---

## Run the Game

From the `day22` directory:

```bash
python main.py
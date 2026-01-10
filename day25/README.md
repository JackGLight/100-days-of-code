# Day 25 — U.S. States Guessing Game

An interactive geography quiz built with Python’s `turtle` and `pandas` libraries.  
Players are prompted to guess U.S. state names, which are displayed on a blank map when answered correctly.

---

## How the Game Works

- A blank map of the United States is displayed
- The player types state names one at a time
- Correct guesses are written onto the map at the proper coordinates
- The game tracks progress out of 50 states
- Typing **"Exit"** ends the game early and generates a study file of missed states

---

## Features

- Interactive text input using Turtle graphics
- State coordinate lookup using a CSV file
- Prevents duplicate answers
- Progress tracking (e.g. `12/50`)
- Automatically generates a practice file for missed states
- Win / exit messages displayed on completion

---

## Controls

- Type a U.S. state name and press Enter
- Type **Exit** to quit early and generate a practice list

---

## Project Structure
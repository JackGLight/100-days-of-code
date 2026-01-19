# Flashcard App (Tkinter)

## Overview
Built a GUI-based flashcard application using Python and Tkinter to practice recognition-based recall from a custom CSV dataset.

## Key Concepts Practiced
- Tkinter UI layout with `Canvas`, images, buttons, and text elements
- Dynamic text rendering for variable-length questions and answers
- Timed UI updates using `window.after()` and `after_cancel()`
- State management for the current flashcard
- CSV data ingestion and persistence with pandas
- Randomized sampling from a dataset
- User-driven progress tracking and file saving

## Features Implemented
- Flashcard front/back flip after a fixed delay
- Visual card state change (image + text color)
- ❌ button to skip a card
- ✅ button to mark a card as known and remove it from future rotation
- Automatic saving of remaining cards to `words_to_learn.csv`
- Resume progress on app restart if saved data exists
- Graceful handling when all cards are completed

## Data Files
- `data/stats.csv`: original question/answer dataset
- `data/words_to_learn.csv`: auto-generated progress file
- Image assets stored in `images/`

## Outcome
Reinforced event-driven programming, GUI state transitions, and persistence of user learning progress in a lightweight desktop application.
# Pomodoro Timer (Tkinter) — Day 28

A simple Pomodoro timer built with **Python and Tkinter** as part of **Day 28** of my *100 Days of Code* challenge.  
The goal of this project was to gain hands-on experience with **event-driven programming**, **UI state management**, and **Tkinter timing mechanisms**.

---

## Features
- 25-minute work sessions  
- 5-minute short breaks  
- 20-minute long break after 4 work sessions  
- Visual countdown timer  
- Checkmarks to track completed work sessions  
- Start and Reset controls  

---

## What I Learned
- Tkinter fundamentals (`Tk`, `Label`, `Button`, `Canvas`)
- Using `after()` for non-blocking timers
- Managing application state with global counters (`reps`)
- Chaining timed callbacks instead of using blocking loops
- Updating existing UI elements dynamically (`config`)
- Properly canceling scheduled callbacks on reset (`after_cancel`)

---

## How It Works
- The timer alternates between **work** and **break** sessions using a session counter (`reps`)
- Each completed work session adds a ✓ to the UI
- The timer uses Tkinter’s `after()` method to update the countdown without freezing the UI
- Reset cancels any scheduled callbacks and restores the initial state

---

## How to Run

### Requirements
- Python 3.x  
- Tkinter (included with standard Python installations)

### Run
```bash
python main.py
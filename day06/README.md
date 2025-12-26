Day 6 – Reeborg's World Maze

Solved the Reeborg’s World maze challenge using Python logic within the
Reeborg simulation environment.

The solution implements the right-hand rule algorithm to navigate an
unknown maze by prioritizing right turns when available, moving forward
when possible, and turning left when blocked.

This code is specific to the Reeborg environment and relies on built-in
functions such as:
- at_goal()
- right_is_clear()
- front_is_clear()
- move()
- turn_left()

Solution logic:

```python
while not at_goal():
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
from tkinter import *
import pandas as pd
import random

# ---------------------------- CONSTANTS ----------------------------
BACKGROUND_COLOR = "#B1DDC6"
FLIP_DELAY_MS = 3000

# ---------------------------- DATA SETUP ----------------------------
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/stats.csv")

data_dict = data.to_dict(orient="records")

current_card = {}
flip_timer = None


# ---------------------------- FUNCTIONS ----------------------------
def set_content_text(text, fill):
    """Wrap + shrink font for long questions/answers."""
    if len(text) > 160:
        font_size = 22
    elif len(text) > 110:
        font_size = 28
    else:
        font_size = 36

    canvas.itemconfig(
        content_text,
        text=text,
        fill=fill,
        font=("Arial", font_size, "bold")
    )


def next_question():
    global current_card, flip_timer

    if not data_dict:
        # No cards left!
        canvas.itemconfig(card_image, image=card_front_img)
        canvas.itemconfig(title_text, text="Done!", fill="black")
        set_content_text("You learned everything 🎉", "black")
        return

    if flip_timer is not None:
        window.after_cancel(flip_timer)

    current_card = random.choice(data_dict)

    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(title_text, text="Question", fill="black")
    set_content_text(str(current_card["Question"]), "black")

    flip_timer = window.after(FLIP_DELAY_MS, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(title_text, text="Answer", fill="white")
    set_content_text(str(current_card["Answer"]), "white")


def known_card():
    """User knows it: remove from list and save remaining to words_to_learn.csv."""
    global data_dict

    # Remove current card from the list
    if current_card in data_dict:
        data_dict.remove(current_card)

    # Save what's left
    pd.DataFrame(data_dict).to_csv("data/words_to_learn.csv", index=False)

    # Move on
    next_question()


def unknown_card():
    """ User doesn't know it: keep it, just move on."""
    next_question()


# ---------------------------- UI SETUP ----------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Images (keep global refs)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

# Card image
card_image = canvas.create_image(400, 263, image=card_front_img)

# Canvas text
title_text = canvas.create_text(
    400, 150,
    text="Title",
    font=("Arial", 40, "italic"),
    fill="black"
)

content_text = canvas.create_text(
    400, 263,
    text="Word",
    font=("Arial", 36, "bold"),
    fill="black",
    width=700,
    justify="center"
)

# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, command=unknown_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0, bd=0, command=known_card)
right_button.grid(row=1, column=1)

# Start
next_question()
window.mainloop()
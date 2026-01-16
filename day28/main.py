import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
check_count = 0
timer_id = None 

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, check_count, timer_id

    # Stop any scheduled countdown callback so reset "sticks"
    if timer_id is not None:
        window.after_cancel(timer_id)
        timer_id = None

    reps = 0
    check_count = 0
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    if reps % 2 == 0:
        count_down(WORK_MIN * 60)
    elif reps < 6:
        count_down(SHORT_BREAK_MIN * 60)
    elif reps == 7:
        count_down(LONG_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, check_count, timer_id

    min_left = int(count / 60)
    str_min_left = str(min_left)
    if min_left < 10:
        str_min_left = '0' + str_min_left

    sec_left = count % 60
    str_sec_left = str(sec_left)
    if sec_left < 10:
        str_sec_left = '0' + str_sec_left

    time_left = f'{str_min_left}:{str_sec_left}'
    canvas.itemconfig(timer_text, text=time_left)

    if count > 0:
        # keep your 1ms testing interval as-is
        timer_id = window.after(1000, count_down, count - 1)
    else:
        reps += 1

        if (reps % 2 != 0) and (reps <= 7):
            check_count += 1

        check_text = "✓" * check_count
        check_mark.config(text=check_text)

        if reps < 8:
            start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(
    100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold')
)
canvas.grid(row=1, column=1)

main_label = tk.Label(
    text="Timer",
    fg=GREEN,
    font=(FONT_NAME, 35, 'bold'),
    highlightthickness=0,
    bg=YELLOW
)
main_label.config(padx=10, pady=10)
main_label.grid(row=0, column=1)

start_button = tk.Button(
    text="Start",
    highlightthickness=0,
    bg=YELLOW,
    command=start_timer
)
start_button.grid(row=2, column=0)

reset_button = tk.Button(
    text="Reset",
    highlightthickness=0,
    bg=YELLOW,
    command=reset_timer
)
reset_button.grid(row=2, column=2)

check_mark = tk.Label(
    text="",
    fg=GREEN,
    font=(FONT_NAME, 35, 'bold'),
    highlightthickness=0,
    bg=YELLOW
)
check_mark.config(padx=10, pady=10)
check_mark.grid(row=3, column=1)

window.mainloop()
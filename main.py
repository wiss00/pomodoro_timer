from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 2
i = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global i
    i = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    global i
    i += 1

    if i % 8 == 0:
        timer.config(text=" break", fg=RED)
        count_down(3)

    elif i % 2 == 0:
        timer.config(text="break", fg=PINK)
        count_down(2)

    else:
        timer.config(text="work", fg=GREEN)
        count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = f"{math.floor(count / 60)}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(i / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)


window = Tk()
window.title("pomodoro timer")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
window.config(padx=100, pady=100, bg=YELLOW)
tomato_img = PhotoImage(file="img.png")
canvas.create_image(100, 100, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Timer")
timer.config(fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
timer.grid(row=0, column=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

checkmark = Label(text="✔", fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark.config(font=(FONT_NAME, 20, "normal"))
checkmark.grid(row=2, column=1)
window.mainloop()

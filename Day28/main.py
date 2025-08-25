import math
from tkinter import *
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
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    word_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="Work Time!", fg=GREEN)
        count_down(word_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
       timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        for _ in range():
            marks += "✓"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



timer_label = Label()
timer_label.config(fg=GREEN,text="Timer", font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

start_btn = Button()
start_btn.config(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

check_mark = Label()
check_mark.config( fg=GREEN, font=(FONT_NAME, 33, "bold"))
check_mark.grid(column=1, row=3)

reset_btn = Button()
reset_btn.config(text="Reset",command=reset_timer)
reset_btn.grid(column=2, row=2)



window.mainloop()
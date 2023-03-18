import tkinter as tk
# import pyttsx3
import math as m

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
RESET_COLOR = '#316B83'
CHECK_LABEL_COLOR = '#362222'
TIMER_LABEL_COLOR = '#206A5D'
FONT_NAME = "Courier"
WORK_COLOR = '#39A388'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ENGINE = pyttsx3.init()


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """This function resets the timer"""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=TIMER_LABEL_COLOR)
    check_label.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    """This function starts the timer"""
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='LONG BREAK', fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='SHORT BREAK', fg=PINK)

    else:
        count_down(work_sec)
        timer_label.config(text='WORK', fg=WORK_COLOR)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """This function counts down the timer"""
    count_min = m.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = '0' + str(count_min)

    if count_sec < 10:
        count_sec = '0' + str(count_sec)
    canvas.itemconfig(timer_text, text=F"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = m.floor(reps / 2)
        for _ in range(work_sessions):
            marks += '☑'
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()

window.title('Day 028: A Pomodoro App')

window.config(padx=100, pady=50, bg=YELLOW)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=2, row=2)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

timer_label = tk.Label(text='TIMER', font=(FONT_NAME, 40, 'bold'), fg=TIMER_LABEL_COLOR, bg=YELLOW, relief='raised')
timer_label.grid(column=2, row=1)

start_label = tk.Button(text='START', font=(FONT_NAME, 20, 'bold'), bg=YELLOW, fg='red', command=start_timer)
start_label.grid(column=1, row=3)

reset_label = tk.Button(text='RESET', font=(FONT_NAME, 20, 'bold'), bg=YELLOW, fg=RESET_COLOR, command=reset_timer)
reset_label.grid(column=3, row=3)

check_label = tk.Label(font=(FONT_NAME, 30, 'bold'), bg=YELLOW, fg=CHECK_LABEL_COLOR)
check_label.grid(column=2, row=3)

window.mainloop()

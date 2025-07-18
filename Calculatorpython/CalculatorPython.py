from tkinter import *

raiz = Tk()
raiz.title("Calculator")
frame = Frame(raiz)
frame.pack()
frame.config(bg="pink", bd="10")

numberp = StringVar()
operation = ""
result = 0.0
clear_screen = False

def displaynumber(num):
    global clear_screen
    if clear_screen:
        numberp.set(num)
        clear_screen = False
    else:
        numberp.set(numberp.get() + num)

def clearInput():
    global result, clear_screen, operation
    numberp.set("")
    result = 0.0
    operation = ""
    clear_screen = False

def set_operation(op):
    global operation, result, clear_screen
    try:
        result = float(numberp.get())
    except ValueError:
        result = 0.0
    operation = op
    clear_screen = True

def results():
    global result, clear_screen, operation
    try:
        current = float(numberp.get())
        if operation == "+":
            result += current
        elif operation == "-":
            result -= current
        elif operation == "*":
            result *= current
        elif operation == "/":
            result = result / current if current != 0 else "Error"
        numberp.set(str(result))
    except:
        numberp.set("Error")
    clear_screen = True

screen = Entry(frame, textvariable=numberp, justify="right", bg="gray", fg="white")
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)

# Buttons layout
buttons = [
    ("7", 2, 1), ("8", 2, 2), ("9", 2, 3), ("/", 2, 4),
    ("4", 3, 1), ("5", 3, 2), ("6", 3, 3), ("*", 3, 4),
    ("1", 4, 1), ("2", 4, 2), ("3", 4, 3), ("-", 4, 4),
    ("0", 5, 1), (".", 5, 2), ("C", 5, 3), ("+", 5, 4),
    ("=", 6, 1)
]

for (text, row, col) in buttons:
    if text in "0123456789.":
        Button(frame, text=text, width=4, command=lambda t=text: displaynumber(t)).grid(row=row, column=col)
    elif text == "C":
        Button(frame, text=text, width=4, command=clearInput).grid(row=row, column=col)
    elif text == "=":
        Button(frame, text=text, width=17, command=results).grid(row=row, column=1, columnspan=4)
    else:
        Button(frame, text=text, width=4, command=lambda t=text: set_operation(t)).grid(row=row, column=col)

raiz.mainloop()
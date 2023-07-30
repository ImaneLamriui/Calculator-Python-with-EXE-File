from tkinter import *
raiz = Tk()
raiz.title("Calculator")
# raiz.iconbitmap(".ico")
# raiz.geometry("300x300")
frame = Frame(raiz)

frame.pack()
# frame.place(x=80, y=40)

# frame.config(width="650", height="450")
frame.config(bg="pink")
frame.config(bd="10")

#globals variable
numberp = StringVar()
operation = ""
result = 0   
resultm = 1
clear_screen = False 


#this function display numbers in the screen
def displaynumber(num):
    global operation
    global clear_screen
    if clear_screen!=False:  
        numberp.set(num)
        clear_screen=False
    else:
        #WRITING series of numbers
        numberp.set(numberp.get() + num) 

#operation function sum +
def sum(num):
    global operation
    global result
    global clear_screen
    result += int(num)
    operation ="sum"
    clear_screen=True
    numberp.set(result)

#operation function subtract-
numr=0
status_resta=0
def rest(num):
    global operation
    global result
    global numr
    global status_resta
    global clear_screen
    if status_resta==0:
        numr=int(num)
        result=numr
    else:
        if status_resta==1:
            result=numr-int(num)
        else:
            result=int(result)-int(num)
        numberp.set(result)
        result=numberp.get()
    status_resta=status_resta+1
    operation ="rest"
    clear_screen=True
   
#operation function multilplication *
status_mult = 0
def mult(num):
    global operation
    global result
    global numr
    global status_mult
    global clear_screen
    if status_mult==0:
        numr=int(num)
        result=numr
    else:
        if status_mult==1:
            result=numr*int(num)
        else:
            result=int(result)*int(num)
        numberp.set(result)
        result=numberp.get()
    status_mult=status_mult+1
    operation ="mult"
    clear_screen=True

#operation function  division /
status_div=0
def div(num):
   
    global clear_screen  
    global operation
    global status_div
    global result
    global numr
    if status_div==0:
        numr=int(num)
        result=numr
    else:
        if status_div==1:
            result=numr//int(num)
        else:
            result=result//int(num)
        numberp.set(result)
        result=numberp.get()
    status_div=status_div+1
    operation = "div"
    clear_screen=True
   
        
#this function clear the  screen
def clearInput():
    global result
    global clear_screen  
    global operation
    
    numberp.set("0")
    result = 0
    clear_screen=1
    operation=""    
  
#funcionamiento de =
def results():
    global result
    global resultm
    global operation
    global status_rest
    global status_div
  
   
    if operation == "suma":
        numberp.set(result+int(numberp.get()))
        result=0
        
    elif operation == "rest":
        numberp.set(int(result)-int(numberp.get()))
        result=0
        status_rest=0
    elif operation =="mult":
        numberp.set(int(resultm)*int(numberp.get()))
        result=0
        status_mult=0
    elif operation=="div":
        numberp.set(int(result)//int(numberp.get()))
        result=0
        status_div=0


#screen row 1
screen = Entry(frame, textvariable = numberp)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=5)
screen.config(background="gray", fg="white", justify="right")

# row 2
number7Button = Button(frame, text="7", width=3, command=lambda:displaynumber("7"))
number7Button.grid(row=2, column=1)
number8Button = Button(frame, text="8", width=3, command=lambda:displaynumber("8"))
number8Button.grid(row=2, column=2)
number9Button = Button(frame, text="9", width=3, command=lambda:displaynumber("9"))
number9Button.grid(row=2, column=3)
divButton = Button(frame, text="/", width=3, command=lambda:div(numberp.get()))
divButton.grid(row=2, column=4)

#Calc Buttons row 3
number4Button = Button(frame, text="4", width=3, command=lambda:displaynumber("4"))
number4Button.grid(row=3, column=1)
number5Button = Button(frame, text="5", width=3, command=lambda:displaynumber("5"))
number5Button.grid(row=3, column=2)
number6Button = Button(frame, text="6", width=3, command=lambda:displaynumber("6"))
number6Button.grid(row=3, column=3)
MultButton = Button(frame, text="x", width=3, command=lambda:mult(numberp.get()))
MultButton.grid(row=3, column=4)

#Calc Buttons row 4
number1Button = Button(frame, text="1", width=3, command=lambda:displaynumber("1"))
number1Button.grid(row=4, column=1)
number2Button = Button(frame, text="2", width=3, command=lambda:displaynumber("2"))
number2Button.grid(row=4, column=2)
number3Button = Button(frame, text="3", width=3, command=lambda:displaynumber("3"))
number3Button.grid(row=4, column=3)
resButton = Button(frame, text="-", width=3, command=lambda:rest(numberp.get()))
resButton.grid(row=4, column=4)

#Calc Buttons row 5
number0Button = Button(frame, text="0", width=3, command=lambda:displaynumber("0"))
number0Button.grid(row=5, column=1)
SumButton = Button(frame, text="+", width=3, command=lambda:sum(numberp.get()))
SumButton.grid(row=5, column=2)
clearButton = Button(frame, text = "C" , width=3, command=lambda:clearInput())
clearButton.grid(row=5, column=3)
iqualButton = Button(frame, text= "=" , width=3, command=lambda:results())
iqualButton.grid(row=5, column=4)


raiz.mainloop()
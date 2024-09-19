from tkinter import *
from tkinter import ttk

global operations, number1, number2, result
operations = ""
number1 = 0 
number2 = 0
result = 1


def refresh():
    global result
    resultsbutton.configure(text= result)

def clear(button):
    global operations, number1, number2, result
    operations = ""
    number1 = 0 
    number2 = 0
    result = 0
    if button:
        refresh()

def operation(symbol):
    global operations
    operations = symbol

def number(num):
    global operations
    if operations == "":
        global number1, result
        number1 *= 10
        number1 += num 
        result = number1
        refresh()

    else:
        global number2
        number2 *= 10
        number2 += num 
        result = number2
        refresh()



def multiply():
    global result
    global number1
    global number2 
    result = number1 * number2

def add():
    global result
    global number1
    global number2 
    result = number1 + number2

def subtract():
    global result
    global number1
    global number2 
    result = number1 - number2

def divide():
    global result
    global number1
    global number2 
    result = number1 / number2


def calculate():
    global operations
    if operations == "x":
        multiply()
    elif operations == "/":
        divide()
    elif operations == "+":
        add()
    elif operations == "-":
        subtract()
    else:
        print("Invalid statement, please retry")
    refresh()
    clear(0)


def start():
    global root
    global resultsbutton

    root = Tk()

    screen= ttk.Frame(root).grid()
    buttons= ttk.Frame(root).grid()

    one = ttk.Button(buttons, text= "1", command= lambda:number(1)).grid(column = 1, row = 3)
    two = ttk.Button(buttons, text= "2", command= lambda:number(2)).grid(column = 2, row = 3)
    three = ttk.Button(buttons, text= "3", command= lambda:number(3)).grid(column = 3, row = 3)
    four = ttk.Button(buttons, text= "4", command= lambda:number(4)).grid(column = 1, row = 4)
    five = ttk.Button(buttons, text= "5", command= lambda:number(5)).grid(column = 2, row = 4)
    six= ttk.Button(buttons, text= "6", command= lambda:number(6)).grid(column = 3, row = 4)
    seven = ttk.Button(buttons, text= "7", command= lambda:number(7)).grid(column = 1, row = 5)
    eight = ttk.Button(buttons, text= "8", command= lambda:number(8)).grid(column = 2, row = 5)
    nine = ttk.Button(buttons, text= "9", command= lambda:number(9)).grid(column = 3, row = 5)
    clr = ttk.Button(buttons, text= "clr",command= lambda:clear(1)).grid(column = 1, row = 6)
    zero = ttk.Button(buttons, text= "0", command= lambda:number(0)).grid(column = 2, row = 6)
    equals= ttk.Button(buttons, text= "=", command= lambda:calculate())
    equals.grid(column = 3, row = 6)
    add = ttk.Button(buttons, text= "+", command= lambda:operation("+") ).grid(column=4, row = 3)
    minus = ttk.Button(buttons, text= "-", command= lambda:operation("-") ).grid(column=4, row = 4)
    multiply = ttk.Button(buttons, text= "x", command= lambda:operation("x") ).grid(column=4, row = 5)
    divide = ttk.Button(buttons, text= "/", command= lambda:operation("/") )
    divide.grid(column=4, row = 6)
    resultsbutton = ttk.Label(screen,text='0')
    resultsbutton.grid(column = 2, row = 1,columnspan = 2 )



    root.mainloop()

start()
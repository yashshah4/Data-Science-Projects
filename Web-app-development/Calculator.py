from tkinter import *
# In mac for the foreground of button to be visible, we need ttk module
from tkinter import ttk
import parser


root = Tk()
root.title("Calculator")

# Get input from user and place it in the display field
# initialising i that store the index of the variables accepted from the user
i = 0
def get_variable(num):
    global i
    display.insert(i, num)
    i+=1
# creating a function to calculate factorial, there is also one in the math module called factorial that one can use
def factorial():
    try:
        f = 1
        equal()
        k = float(display.get())
        for j in range(k,0,-1):
            f*=j
        clear_all()
        display.insert(0, str(f))
    except :
# creating a function that clears the display field

def clear_all():
    display.delete(0, END)
# creating a funtion that deletes one element at a time
def del_one():
    global i
    display.delete(i-1,i)
    i-=1
    if i==0:
        clear_all()
# creating a function that evaluates the input expression and prints the result
def equal():
    try:
       result = eval(parser.expr(display.get()).compile())
       clear_all()
       display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
# Creating a function to diplay the operator
def disp_op(operator):
    global i
    display.insert(i, operator)
    i+=len(operator)
# Creating the display area on the calculator app
display = Entry(root)
# The sticky keyword takes input west to east so that the display spans from end to end of the window
display.grid(row=0, columnspan=6, sticky=W+E)

# Creating buttons for the calculator
ttk.Button(root, text="1", command = lambda : get_variable(1)).grid(row=1, column=0)
ttk.Button(root, text="2", command = lambda : get_variable(2)).grid(row=1, column=1)
ttk.Button(root, text="3", command = lambda : get_variable(3)).grid(row=1, column=2)

ttk.Button(root, text="4", command = lambda : get_variable(4)).grid(row=2, column=0)
ttk.Button(root, text="5", command = lambda : get_variable(5)).grid(row=2, column=1)
ttk.Button(root, text="6", command = lambda : get_variable(6)).grid(row=2, column=2)

ttk.Button(root, text="7", command = lambda : get_variable(7)).grid(row=3, column=0)
ttk.Button(root, text="8", command = lambda : get_variable(8)).grid(row=3, column=1)
ttk.Button(root, text="9", command = lambda : get_variable(9)).grid(row=3, column=2)

# creating additional buttons

ttk.Button(root, text="AC", command=clear_all).grid(row=4, column=0)
ttk.Button(root, text="0", command = lambda : get_variable(0)).grid(row=4, column=1)
ttk.Button(root, text="=", command= lambda:equal()).grid(row=4, column=2)

# creating functional buttons

ttk.Button(root, text="DEL", command=del_one).grid(row=1, column=3)
ttk.Button(root, text="+", command=lambda: disp_op("+")).grid(row=2, column=3)
ttk.Button(root, text="*", command=lambda: disp_op("*")).grid(row=3, column=3)
ttk.Button(root, text="(", command=lambda: disp_op("(")).grid(row=4, column=3)

ttk.Button(root, text="!", command=lambda: factorial()).grid(row=1, column=4)
ttk.Button(root, text="-", command=lambda: disp_op("-")).grid(row=2, column=4)
ttk.Button(root, text="/", command=lambda: disp_op("/")).grid(row=3, column=4)
ttk.Button(root, text=")", command=lambda: disp_op(")")).grid(row=4, column=4)

ttk.Button(root, text="%", command=lambda: disp_op("%")).grid(row=1, column=5)
ttk.Button(root, text="exp", command=lambda: disp_op("**")).grid(row=2, column=5)
ttk.Button(root, text="Sq root", command=lambda: disp_op("**0.5")).grid(row=3, column=5)
ttk.Button(root, text="//", command=lambda: disp_op("//")).grid(row=4, column=5)

root.mainloop()
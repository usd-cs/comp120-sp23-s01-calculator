"""
GUI for Calcul8r Alig8r: the awesomest calculator app in existence.
"""

import tkinter as tk
from tkinter import ttk

"""
The following are simple examples for creating a label and a button.

my_label = tk.Label(container, text="Hello World")
my_button = tk.Button(container, text="Click Me!")

The following links will be useful for helping you customize your labels and
buttons.

Labels: https://tkdocs.com/shipman/label.html
Buttons: https://tkdocs.com/shipman/button.html
"""

def append0():
    display['text'] += '0'

def append1():
    display['text'] += '1'

def append2():
    display['text'] += '2'

def append3():
    display['text'] += '3'

def append4():
    display['text'] += '4'

def append5():
    display['text'] += '5'

def append6():
    display['text'] += '6'

def append7():
    display['text'] += '7'

def append8():
    display['text'] += '8'

def append9():
    display['text'] += '9'

# Create the application window
window = tk.Tk()
window.title("Calcul8r Alig8r")



# Create Frame to hold the number display and undo/clear buttons
display_frame = tk.Frame(window)
display_frame.grid(row=0, column=0, columnspan=5)


# create number display (a Label) and clear/undo buttons and place them
# within the display_frame using the grid layout manager

display = tk.Label(display_frame, bg="white", fg="black", text="0", width=15, height=2)
undo = tk.Button(display_frame, text="Undo")
clear = tk.Button(display_frame,text="Clear")
display.grid(row=0, column=0, columnspan=4, rowspan=2)
undo.grid(row=0, column=4)
clear.grid(row=1, column=4)


# Create Frame to hold the operator (e.g. +, -, ...) buttons
operators_frame = tk.Frame(window)
operators_frame.grid(row=1, column=0, columnspan=5)


# create operator buttons and place them within the operators_frame using
# the grid layout manager

plus =  tk.Button(operators_frame, text= "+")
plus.grid(row=1, column=1)
minus = tk.Button(operators_frame, text="-")
minus.grid(row=1, column=2)
divide = tk.Button(operators_frame,text= "/")
divide.grid(row=1, column=3)
time = tk.Button(operators_frame, text ="x")
time.grid(row=1, column=4)
expo = tk.Button(operators_frame, text ="^")
expo.grid(row=1, column=5)


# Create Frame to hold the number and = buttons
numbers_frame = tk.Frame(window)
numbers_frame.grid(row=2, column=0, columnspan=4)


# create number and = buttons and place them within the numbers_frame using
# the grid layout manager

equal = tk.Button(numbers_frame, text="=")
one = tk.Button(numbers_frame, text="1", command=append1)
two = tk.Button(numbers_frame, text="2", command=append2)
three = tk.Button(numbers_frame, text="3", command=append3)
four = tk.Button(numbers_frame, text="4", command=append4)
five = tk.Button(numbers_frame, text="5", command=append5)
six = tk.Button(numbers_frame, text="6", command=append6)
seven = tk.Button(numbers_frame, text="7", command=append7)
eight = tk.Button(numbers_frame, text="8", command=append8)
nine = tk.Button(numbers_frame, text="9", command=append9)
zero = tk.Button(numbers_frame, text="0", command=append0)

seven.grid(row = 0,column = 0)
eight.grid(row = 0,column = 1)
nine.grid(row = 0,column = 2)
four.grid(row = 1,column = 0)
five.grid(row = 1,column = 1)
six.grid(row = 1,column = 2)
one.grid(row = 2,column = 0)
two.grid(row = 2,column = 1)
three.grid(row = 2,column = 2)
zero.grid(row = 3,column = 0, columnspan = 2, sticky = "we")
equal.grid(row = 3,column = 2)


# Start the GUI event loop
window.mainloop() 

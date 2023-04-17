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

class CalculatorApp(tk.Tk):
    def set_commands(self):
        def append0():
            self.display['text'] += '0'

        def append1():
            self.display['text'] += '1'

        def append2():
            self.display['text'] += '2'

        def append3():
            self.display['text'] += '3'

        def append4():
            self.display['text'] += '4'

        def append5():
            self.display['text'] += '5'

        def append6():
            self.display['text'] += '6'

        def append7():
            self.display['text'] += '7'

        def append8():
            self.display['text'] += '8'

        def append9():
            self.display['text'] += '9'

        self.zero_button['command'] = append0
        self.one_button['command'] = append1
        self.two_button['command'] = append2
        self.three_button['command'] = append3
        self.four_button['command'] = append4
        self.five_button['command'] = append5
        self.six_button['command'] = append6
        self.seven_button['command'] = append7
        self.eight_button['command'] = append8
        self.nine_button['command'] = append9


    # Create the application window
    #window = tk.Tk()

    def __init__(self):
        super().__init__()
        self.title("Calcul8r Alig8r")
        self.create_layout()
        self.set_commands()

    def create_layout(self):
        # Create Frame to hold the number display and undo/clear buttons
        display_frame = tk.Frame(self)
        display_frame.grid(row=0, column=0, columnspan=5)

        # create number display (a Label) and clear/undo buttons and place them
        # within the display_frame using the grid layout manager

        self.display = tk.Label(display_frame, bg="white", fg="black", text="0", width=15, height=2)
        self.undo = tk.Button(display_frame, text="Undo")
        self.clear = tk.Button(display_frame,text="Clear")
        self.display.grid(row=0, column=0, columnspan=4, rowspan=2)
        self.undo.grid(row=0, column=4)
        self.clear.grid(row=1, column=4)

        # Create Frame to hold the operator (e.g. +, -, ...) buttons
        operators_frame = tk.Frame(self)
        operators_frame.grid(row=1, column=0, columnspan=5)


        # create operator buttons and place them within the operators_frame using
        # the grid layout manager

        self.plus =  tk.Button(operators_frame, text= "+")
        self.plus.grid(row=1, column=1)
        self.minus = tk.Button(operators_frame, text="-")
        self.minus.grid(row=1, column=2)
        self.divide = tk.Button(operators_frame,text= "/")
        self.divide.grid(row=1, column=3)
        self.multiply = tk.Button(operators_frame, text ="x")
        self.multiply.grid(row=1, column=4)
        self.power = tk.Button(operators_frame, text ="^")
        self.power.grid(row=1, column=5)

        # Create Frame to hold the number and = buttons
        numbers_frame = tk.Frame(self)
        numbers_frame.grid(row=2, column=0, columnspan=4)

        # create number and = buttons and place them within the numbers_frame using
        # the grid layout manager

        self.equal_button = tk.Button(numbers_frame, text="=")
        self.one_button = tk.Button(numbers_frame, text="1")
        self.two_button = tk.Button(numbers_frame, text="2")
        self.three_button = tk.Button(numbers_frame, text="3")
        self.four_button = tk.Button(numbers_frame, text="4")
        self.five_button = tk.Button(numbers_frame, text="5")
        self.six_button = tk.Button(numbers_frame, text="6")
        self.seven_button = tk.Button(numbers_frame, text="7")
        self.eight_button = tk.Button(numbers_frame, text="8")
        self.nine_button = tk.Button(numbers_frame, text="9")
        self.zero_button = tk.Button(numbers_frame, text="0")

        # top row of numbers
        self.seven_button.grid(row = 0,column = 0)
        self.eight_button.grid(row = 0,column = 1)
        self.nine_button.grid(row = 0,column = 2)

        # second row of numbers
        self.four_button.grid(row = 1,column = 0)
        self.five_button.grid(row = 1,column = 1)
        self.six_button.grid(row = 1,column = 2)

        # third row of numbers
        self.one_button.grid(row = 2,column = 0)
        self.two_button.grid(row = 2,column = 1)
        self.three_button.grid(row = 2,column = 2)

        # bottom row of numbers (and =)
        self.zero_button.grid(row = 3,column = 0, columnspan = 2, sticky = "we")
        self.equal_button.grid(row = 3,column = 2)


app = CalculatorApp()
app.mainloop() # Start the GUI event loop
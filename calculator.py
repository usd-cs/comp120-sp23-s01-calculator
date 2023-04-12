"""
GUI for the awesomest calculator app in existence.
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


# Create the application window
window = tk.Tk()

# Create Frame to hold the number display and undo/clear buttons
display_frame = tk.Frame()
display_frame.grid(row=0, column=0, columnspan=5)


# TODO: create number display (a Label) and clear/undo buttons and place them
# within the display_frame using the grid layout manager


# Create Frame to hold the operator (e.g. +, -, ...) buttons
operators_frame = tk.Frame()
operators_frame.grid(row=1, column=0, columnspan=5)


# TODO: create operator buttons and place them within the operators_frame using
# the grid layout manager


# Create Frame to hold the number and = buttons
numbers_frame = tk.Frame()
numbers_frame.grid(row=2, column=0, columnspan=4)


# TODO: create number and = buttons and place them within the numbers_frame using
# the grid layout manager



# Start the GUI event loop
window.mainloop() 

# Import the Tkinter module
from tkinter import *

# Create a window object
window = Tk()

# Set the window title and size
window.title("Calculator")
window.geometry("300x300")

# Create a variable to store the expression
expression = ""

# Create a function to update the expression
def update_expression(num):
    global expression
    expression += str(num)
    display.set(expression)

# Create a function to evaluate the expression
def evaluate_expression():
    global expression
    try:
        result = str(eval(expression))
        display.set(result)
    except:
        display.set("Error")
    expression = ""

# Create a function to clear the expression
def clear_expression():
    global expression
    expression = ""
    display.set("")

# Create a display widget
display = StringVar()
display.set("")
display_label = Label(window, textvariable=display, font=("Arial", 20), bg="white", width=14, anchor="e")
display_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Create the buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Add the buttons to the window
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        button = Button(window, text=buttons[i][j], font=("Arial", 16), width=4, command=lambda x=buttons[i][j]: update_expression(x) if x not in ["=", "C"] else evaluate_expression() if x == "=" else clear_expression())
        button.grid(row=i+1, column=j, padx=5, pady=5)

# Start the main loop
window.mainloop()

import tkinter as tk
from tkinter import messagebox

# create a tkinter window
root = tk.Tk()

# set the window title
root.title("Hello World")

# create a function to show the alert message
def show_alert():
    messagebox.showinfo("Alert", "Hello world")

# create a button and attach the show_alert function to its click event
btn = tk.Button(root, text="Click me", command=show_alert)

# add the button to the window
btn.pack()

# start the tkinter event loop
root.mainloop()

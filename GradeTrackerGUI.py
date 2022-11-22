from urllib import request
from tkinter import *

import tkinter as tk

root = tk.Tk()
window = tk.Tk()
window.title("Grade Tracker")

frame = tk.Frame(window)
frame.pack()

root.geometry("650x650")
result_text = tk.Text(root, height=3, width=16, font=("Arial", 24))
def click():
    hello = "Grade is " + e.get()
    Labels= Label(root, text=hello)
    Labels.pack()
e = Entry(root, width=40, bg="green")

Buttons1 = Button(root, text="Enter the Grade to Python Absolute Beginner Module 1", command=click)
Buttons2 = Button(root, text="Enter the Grade to Python Absolute Beginner Module 2", command=click)
Buttons1.pack()
e.pack()
Buttons2.pack()
e.pack()


root.mainloop()
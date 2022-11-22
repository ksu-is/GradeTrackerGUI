from urllib import request
from tkinter import *

import tkinter as tk

root = tk.Tk()

root.geometry("650x650")
result_text = tk.Text(root, height=3, width=16, font=("Arial", 24))
e = Entry(root, width=40, bg="green")
e.pack()

def click():
    hello = "Grade is " + e.get()
    Labels= Label(root, text=hello)
    Labels.pack()
root.mainloop()
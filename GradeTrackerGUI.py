import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Grade Tracker")

frame = tk.Frame(window)
frame.pack()

info_user = tk.LabelFrame(frame, text="Python Course (1 & 2")
info_user.grid(row=0, column=0, padx=20, pady=20)

python_1_module_1 = tk.Label(info_user, text="Python 1 Module 1")
python_1_module_1.grid(row=0, column=0)
python_1_module_2=tk.Label(info_user, text="Python 1 Module 2" )
python_1_module_2.grid(row=2, column=0)
python_1_module_3=tk.Label(info_user, text="Python 1 Module 3" )
python_1_module_3.grid(row=4, column=0)
python_1_module_4=tk.Label(info_user, text="Python 1 Module 4" )
python_1_module_4.grid(row=6, column=0)
python_1_module_5=tk.Label(info_user, text="Python 1 Module 5" )
python_1_module_5.grid(row=8, column=0)
python_2_module_1 = tk.Label(info_user, text="Python 2 Module 1")
python_2_module_1.grid(row=10, column=0)
python_2_module_2 = tk.Label(info_user, text="Python 2 Module 2")
python_2_module_2.grid(row=12, column=0)
python_2_module_3 = tk.Label(info_user, text="Python 2 Module 3")
python_2_module_3.grid(row=14, column=0)
python_2_module_4 = tk.Label(info_user, text="Python 2 Module 4")
python_2_module_4.grid(row=16, column=0)
python_2_module_5 = tk.Label(info_user, text="Python 2 Module 5")
python_2_module_5.grid(row=18, column=0)

python_1_module_1 = tk.Entry(info_user)
python_1_module_1.grid(row=1, column=0)
python_1_module_2 = tk.Entry(info_user)
python_1_module_2.grid(row=3, column=0)
python_1_module_3 = tk.Entry(info_user)
python_1_module_3.grid(row=5, column=0)
python_1_module_4 = tk.Entry(info_user)
python_1_module_4.grid(row=7, column=0)
python_1_module_5 = tk.Entry(info_user)
python_1_module_5.grid(row=9, column=0)
python_2_module_1 = tk.Entry(info_user)
python_2_module_1.grid(row=11,column=0)
python_2_module_2 = tk.Entry(info_user)
python_2_module_2.grid(row=13,column=0)
python_2_module_3 = tk.Entry(info_user)
python_2_module_3.grid(row=15,column=0)
python_2_module_4 = tk.Entry(info_user)
python_2_module_4.grid(row=17,column=0)
python_2_module_5 = tk.Entry(info_user)
python_2_module_5.grid(row=19,column=0)





window.mainloop()
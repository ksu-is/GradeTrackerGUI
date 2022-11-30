import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Grade Tracker")

frame = tk.Frame(window)
frame.pack()

info_user = tk.LabelFrame(frame, text="Grades")
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

letter_grade = tk.Label(info_user, text="Letter Grade")
letter_grade_box = ttk.Combobox(info_user, values=["A", "B", "C", "D", "F"])
letter_grade.grid(row=0, column=2)
letter_grade_box.grid(row=1, column=2)


window.mainloop()
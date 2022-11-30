import tkinter as tk

window = tk.Tk()
window.title("Grade Tracker")

frame = tk.Frame(window)
frame.pack()

info_user = tk.LabelFrame(frame, text="Grades")
info_user.grid(row=0, column=0)

python_1_module_1 = tk.Label(info_user, text="Python 1 Module 1")
python_1_module_1.grid(row=0, column=0)
python_1_module_2=tk.Label(info_user, text="Python 1 Module 2" )
python_1_module_2.grid(row=2, column=0)

python_1_module_1 = tk.Entry(info_user)
python_1_module_1.grid(row=1, column=0)
python_1_module_2 = tk.Entry(info_user)
python_1_module_2.grid(row=4, column=0)

window.mainloop()
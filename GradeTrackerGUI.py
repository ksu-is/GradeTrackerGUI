import tkinter as tk
import os
from tkinter import *
from tkinter import font
import openpyxl


def excel_data():
    P1M1 = python_1_module_1.get()
    P1M2 = python_1_module_2.get()
    P1M3 = python_1_module_3.get()
    P1M4 = python_1_module_4.get()
    P1M5 = python_1_module_5.get()
    P2M1 = python_2_module_1.get()
    P2M2 = python_2_module_2.get()
    P2M3 = python_2_module_3.get()
    P2M4 = python_2_module_4.get()
    P2M5 = python_2_module_5.get()
    print("P1M1 Grade:", P1M1, "P1M2 Grade:", P1M2, "P1M3 Grade:", P1M3, "P1M4 Grade:", P1M4, "P1M5 Grade:", P1M5)
    print("P2M1 Grade:", P2M1, "P2M2 Grade:", P2M2, "P2M3 Grade:", P2M3, "P2M4 Grade:", P2M4, "P2M5 Grade:", P2M5)

    filepath_excel = r"C:\Users\danie\Downloads\ExcelPython.xlsx"
    #Note: Make a new file in front of the .xlsx. This will utilize the below funtion ann create an excel file with heading. 
    #Note: If file is already created, it will be updated

    if not os.path.exists(filepath_excel):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ["P1M1", "P1M2", "P1M3", "P1M4", "P1M5", "P2M1", "P2M2", "P2M3", "P2M4", "P2M5"]
        sheet.append(heading)
        workbook.save(filepath_excel)
    workbook = openpyxl.load_workbook(filepath_excel)
    excel_sheet = workbook.active
    excel_sheet.append([P1M1, P1M2, P1M3, P1M4, P1M5, P2M1, P2M2, P2M3, P2M4, P2M5])
    workbook.save(filepath_excel)

window = tk.Tk()
window.title("Grade Tracker")
window.geometry = ("1200x710")

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

button_press = tk.Button(frame, text= "Submit Grades", command= excel_data)
button_press.grid(row=3, column=0, sticky="news", padx=15, pady=10)

window.mainloop()
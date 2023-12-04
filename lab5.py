import tkinter as tk
import subprocess

def open_calc1_window():
    command = 'python LossOfLifeCalculator.py'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(result.stderr)

def open_calc2_window():
    command = 'python GeneralLoss.py'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(result.stderr)


root = tk.Tk()
root.title("Калькулятори збитків")

label = tk.Label(root, text="Eко-моніторинг лабораторні роботи")
label.pack()

lab1_button = tk.Button(root, text="Збитки втрат життя та здоров'я населення", command=open_calc1_window)
lab1_button.pack(side=tk.LEFT, padx=5)

lab2_button = tk.Button(root, text="Збитки основних фондів, знищення майна та продукції", command=open_calc2_window)
lab2_button.pack(side=tk.LEFT, padx=5)


root.mainloop()

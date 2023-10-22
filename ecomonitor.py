import tkinter as tk
import subprocess

def open_lab1_window():
    command = 'python lab1.py'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(result.stderr)

def open_lab2_window():
    lab2_window = tk.Toplevel(root)
    lab2_window.title("Eко-моніторинг Лабораторна 2")

def open_lab3_window():
    lab3_window = tk.Toplevel(root)
    lab3_window.title("Eко-моніторинг Лабораторна 3")


def open_lab4_window():
    lab4_window = tk.Toplevel(root)
    lab4_window.title("Eко-моніторинг Лабораторна 4")


def open_lab5_window():
    lab4_window = tk.Toplevel(root)
    lab4_window.title("Eко-моніторинг Лабораторна 5")


root = tk.Tk()
root.title("Eко-моніторинг лаби")

label = tk.Label(root, text="Eко-моніторинг лабораторні роботи")
label.pack()

lab1_button = tk.Button(root, text="Lab1", command=open_lab1_window)
lab1_button.pack(side=tk.LEFT, padx=5)

lab2_button = tk.Button(root, text="Lab2", command=open_lab2_window)
lab2_button.pack(side=tk.LEFT, padx=5)

lab3_button = tk.Button(root, text="Lab3", command=open_lab3_window)
lab3_button.pack(side=tk.LEFT, padx=5)

lab4_button = tk.Button(root, text="Lab4", command=open_lab4_window)
lab4_button.pack(side=tk.LEFT, padx=5)

lab5_button = tk.Button(root, text="Lab5", command=open_lab5_window)
lab5_button.pack(side=tk.LEFT, padx=5)

root.mainloop()

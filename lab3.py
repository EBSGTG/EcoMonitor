import tkinter as tk
from tkinter import ttk
import mysql.connector
from enum import Enum

# Оголошення ENUM для objectName та pollutantName
class ObjectName(Enum):
    PTAHOKOMPLEX_GUBIN = 'ТзОВ «Птахокомплекс Губин»'
    LOKACHYNSKIY_CVNTK = 'Локачинський ЦВНТК ПАТ «Укргазвидобування»'
    VOLYNTORF = 'ДП «Волиньторф»'
    FREE = 'FREE'

# З'єднання з базою даних
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1809",
    database="ecomon"
)

cursor = db.cursor()

# Функція для розрахунку відшкодування та збереження в базу даних
def calculate_compensation():
    object_name = object_combobox.get()
    pollutant_name = pollutant_combobox.get()
    gdk_g = float(gdk_g_entry.get())
    gdk_your = float(gdk_your_entry.get())
    volume = float(volume_entry.get())
    time = float(time_entry.get())
    min_salary = float(min_salary_entry.get())
    index_danger = float(index_danger_entry.get())
    c_t = float(c_t_entry.get())
    c_danger = float(c_danger_entry.get())

    # Розрахунок розміру відшкодування (можна замінити на власний розрахунок)
    weight = 3.6 * pow(10, -6) * (gdk_g - gdk_your) * volume * time
    compensation_amount = weight * 1.1 * min_salary * index_danger * c_t * c_danger

    # Вивід розрахунку на екран
    result_var.set(f"Розмір відшкодування: {compensation_amount:.5f}")

    # Збереження даних у базі даних
    query = (
        "INSERT INTO compensation_data "
        "(object_name, pollutant_name, gdk_g, gdk_your, volume, time, weight, min_salary, index_danger, c_t, c_danger, compensation_amount) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )
    values = (
        object_name, pollutant_name, gdk_g, gdk_your, volume, time, weight,
        min_salary, index_danger, c_t, c_danger, compensation_amount
    )
    cursor.execute(query, values)
    db.commit()  # Оновлення бази даних

# Створення головного вікна
root = tk.Tk()
root.title("Розрахунок відшкодування збитків")

# Створення та розміщення елементів на головному вікні
object_label = tk.Label(root, text="Назва об'єкта:")
object_label.pack()

object_combobox = ttk.Combobox(root, values=[obj.value for obj in ObjectName], state="readonly")
object_combobox.pack()

pollutant_label = tk.Label(root, text="Тип субстанції:")
pollutant_label.pack()

pollutant_combobox = ttk.Combobox(root, values=["SO2", "NO2", "CO"], state="readonly")
pollutant_combobox.pack()

gdk_g_label = tk.Label(root, text="Значення  затвердженого  граничнодопустимого  викиду:")
gdk_g_label.pack()

gdk_g_entry = tk.Entry(root)
gdk_g_entry.pack()

gdk_your_label = tk.Label(root, text="Значення    граничнодопустимого    викиду:")
gdk_your_label.pack()

gdk_your_entry = tk.Entry(root)
gdk_your_entry.pack()

volume_label = tk.Label(root, text="Значення  об'ємної  витрати  газопилового  потоку   від v:")
volume_label.pack()

volume_entry = tk.Entry(root)
volume_entry.pack()

time_label = tk.Label(root, text="Час роботи джерела викиду i-тої забруднюючої  речовини")
time_label.pack()

time_entry = tk.Entry(root)
time_entry.pack()

min_salary_label = tk.Label(root, text="Мінімальна зарплата:")
min_salary_label.pack()

min_salary_entry = tk.Entry(root)
min_salary_entry.pack()

index_danger_label = tk.Label(root, text="Безрозмірний  показник  відносної  небезпечності:")
index_danger_label.pack()

index_danger_entry = tk.Entry(root)
index_danger_entry.pack()

c_t_label = tk.Label(root, text="Коефіцієнт, що враховує територіальні соціально-екологічні особливості:")
c_t_label.pack()

c_t_entry = tk.Entry(root)
c_t_entry.pack()

c_danger_label = tk.Label(root, text="Коефіцієнт,   що   залежить   від  рівня  забрудненнязіатмосферного  повітря   населеного   пункту   i-тою   забруднюючою речовиною:")
c_danger_label.pack()

c_danger_entry = tk.Entry(root)
c_danger_entry.pack()

calculate_button = tk.Button(root, text="Розрахувати відшкодування", command=calculate_compensation)
calculate_button.pack()

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

def show_history():
    cursor.execute("SELECT * FROM compensation_data")
    data = cursor.fetchall()

    history_window = tk.Toplevel(root)
    history_window.title("Історія")

    def display_compensation_data():
        treeview.delete(*treeview.get_children())

        cursor.execute("SELECT * FROM compensation_data")
        data = cursor.fetchall()

        for row in data:
            treeview.insert("", "end", values=row)

    treeview = ttk.Treeview(history_window, columns=("ID", "Object Name", "Pollutant Name", "GDK G", "GDK Your", "Volume", "Time", "Weight", "Min Salary", "Index Danger", "C T", "C Danger", "Compensation Amount"))
    treeview.heading("#1", text="ID", anchor="w")
    treeview.heading("#2", text="Назва об'єкту", anchor="w")
    treeview.heading("#3", text="Назва субстанції", anchor="w")
    treeview.heading("#4", text="PO(B1)", anchor="w")
    treeview.heading("#5", text="PO(B2)", anchor="w")
    treeview.heading("#6", text="q", anchor="w")
    treeview.heading("#7", text="T", anchor="w")
    treeview.heading("#8", text="M(i)", anchor="w")
    treeview.heading("#9", text="П", anchor="w")
    treeview.heading("#10", text="А(і)", anchor="w")
    treeview.heading("#11", text="К(т)", anchor="w")
    treeview.heading("#12", text="К(зі)", anchor="w")
    treeview.heading("#13", text="Розмір збитків", anchor="w")

    treeview.pack()

    display_compensation_data()

    refresh_button = tk.Button(history_window, text="Оновити", command=display_compensation_data)
    refresh_button.pack()

# Створення головного вікна

history_button = tk.Button(root, text="Історія", command=show_history)
history_button.pack()

# Запуск головного циклу
root.mainloop()

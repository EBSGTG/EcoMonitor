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

class PollutantName(Enum):
    NO2 = 'NO2'
    SO2 = 'SO2'
    CO = 'CO'

# З'єднання з базою даних
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1809",
    database="ecomon"
)

cursor = db.cursor()

# Функція для розрахунку kr і оновлення бази даних
def calculate_kr():
    object_name = object_combobox.get()
    pollutant_name = pollutant_combobox.get()
    ca = float(input_entries["ca"].get())
    ch = float(input_entries["ch"].get())
    tout = float(input_entries["tout"].get())
    tin = float(input_entries["tin"].get())
    vout = float(input_entries["vout"].get())
    vin = float(input_entries["vin"].get())
    ef = float(input_entries["ef"].get())
    ed = float(input_entries["ed"].get())
    bw = float(input_entries["bw"].get())
    at = float(input_entries["at"].get())

    kr = ((ca*tout*vout)+(ch*tin*vin)*ef*ed)/(bw*at*365)

    if kr > 0.001:
        level = "Високий"
    elif 0.0001 < kr < 0.001:
        level = "Середній"
    elif 0.000001 < kr < 0.0001:
        level = "Низький"
    elif kr < 0.000001:
        level = "Бажаний"

    kr_result.config(text=f"kr: {kr:.6f}, Рівень Небезпеки: {level}")

    # Збереження даних у базі даних
    query = "INSERT INTO data_calculations_kr (objectName, pollutantName, ca, ch, tout, tin, vout, vin, ef, ed, bw, at, kr,level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
    values = (object_name, pollutant_name, ca, ch, tout, tin, vout, vin, ef, ed, bw, at, kr, level)
    cursor.execute(query, values)
    db.commit()  # Оновлення бази даних


# Створення головного вікна
root = tk.Tk()
root.title("Розрахунок kr")

# Створення та розміщення елементів на головному вікні
object_label = tk.Label(root, text="Назва об'єкта:")
object_label.pack()

object_combobox = ttk.Combobox(root, values=[obj.value for obj in ObjectName], state="readonly")
object_combobox.pack()

pollutant_label = tk.Label(root, text="Тип субстанції:")
pollutant_label.pack()

pollutant_combobox = ttk.Combobox(root, values=[poll.value for poll in PollutantName], state="readonly")
pollutant_combobox.pack()

# Створення та розміщення полів для вводу даних
input_labels = ["ca", "ch", "tout", "tin", "vout", "vin", "ef", "ed", "bw", "at"]
input_entries = {}

for label_text in input_labels:
    label_frame = tk.Frame(root)
    label_frame.pack(fill=tk.X)

    label_widget = tk.Label(label_frame, text=label_text, anchor="center")  # Center align the text
    label_widget.pack(side=tk.LEFT, fill=tk.X)

    entry_frame = tk.Frame(root)
    entry_frame.pack(fill=tk.X)

    entry_widget = tk.Entry(entry_frame)
    entry_widget.pack(side=tk.LEFT, fill=tk.X, expand=True)

    input_entries[label_text] = entry_widget


# Кнопка для розрахунку
calculate_button = tk.Button(root, text="Розрахувати kr", command=calculate_kr)
calculate_button.pack()

def display_data_calculations_kr():
    treeview.delete(*treeview.get_children())  # Clear the existing data

    cursor.execute("SELECT * FROM data_calculations_kr")
    data = cursor.fetchall()

    for row in data:
        treeview.insert("", "end", values=row)

kr_result = tk.Label(root, text="")
kr_result.pack()


def show_history():
    cursor.execute("SELECT * FROM data_calculations_kr")
    data = cursor.fetchall()

    # Create a new window for displaying the historical table
    history_window = tk.Toplevel(root)
    history_window.title("Історія")

    # Create a Treeview widget to display the table
    treeview = ttk.Treeview(history_window, columns=("Object Name", "Pollutant Name", "ca", "ch", "tout", "tin", "vout", "vin", "ef", "ed", "bw", "at", "kr", "level"))
    treeview.heading("#0", text="ID")
    treeview.heading("#1", text="Назва об'єкту")
    treeview.heading("#2", text="Назва субстанції")
    treeview.heading("#3", text="Концентрація речовини в атмосферному повітрі, мг/куб.м")
    treeview.heading("#4", text="Концентрація речовини у повітрі приміщення, мг/куб.м")
    treeview.heading("#5", text="Час, що проводиться поза приміщенням, год/доба")
    treeview.heading("#6", text="Час, що проводиться у приміщенні, год/доба")
    treeview.heading("#7", text="Швидкість дихання поза приміщенням, куб.м/год")
    treeview.heading("#8", text="Швидкість дихання у приміщенні, куб.м/год")
    treeview.heading("#9", text="Частота впливу, днів/рік")
    treeview.heading("#10", text="Тривалість впливу, років")
    treeview.heading("#11", text="Маса тіла, кг")
    treeview.heading("#12", text="Період осереднення експозиції, років")
    treeview.heading("#13", text="kr")
    treeview.heading("#14", text="level")
    treeview.column("#0", width=0)
    treeview.pack()

    for row in data:
        treeview.insert("", "end", values=row)

    treeview.pack()



history_button = tk.Button(root, text="Історія", command=show_history)
history_button.pack()


# Запуск головного циклу
root.mainloop()

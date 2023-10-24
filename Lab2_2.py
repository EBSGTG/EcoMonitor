import tkinter as tk
from tkinter import ttk
import mysql.connector
from enum import Enum

class ObjectName(Enum):
    PTAHOKOMPLEX_GUBIN = 'ТзОВ «Птахокомплекс Губин»'
    LOKACHYNSKIY_CVNTK = 'Локачинський ЦВНТК ПАТ «Укргазвидобування»'
    VOLYNTORF = 'ДП «Волиньторф»'
    FREE = 'FREE'

class PollutantName(Enum):
    NO2 = 'NO2'
    SO2 = 'SO2'
    CO = 'CO'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1809",
    database="ecomon"
)

cursor = db.cursor()

def calculate_kr():
    object_name = object_combobox.get()
    pollutant_name = pollutant_combobox.get()
    ca = float(input_entries["Концентрація речовини в атмосферному повітрі, мг/куб.м"].get())
    ch = float(input_entries["Концентрація речовини у повітрі приміщення, мг/куб.м"].get())
    tout = float(input_entries["Час, що проводиться поза приміщенням, год/доба"].get())
    tin = float(input_entries["Час, що проводиться у приміщенні, год/доба"].get())
    vout = float(input_entries["Швидкість дихання поза приміщенням, куб.м/год"].get())
    vin = float(input_entries["Швидкість дихання у приміщенні, куб.м/год"].get())
    ef = float(input_entries["Частота впливу, днів/рік"].get())
    ed = float(input_entries["Тривалість впливу, років"].get())
    bw = float(input_entries["Маса тіла, кг"].get())
    at = float(input_entries["Період осереднення експозиції, років"].get())

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

    query = "INSERT INTO data_calculations_kr (objectName, pollutantName, ca, ch, tout, tin, vout, vin, ef, ed, bw, at, kr,level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
    values = (object_name, pollutant_name, ca, ch, tout, tin, vout, vin, ef, ed, bw, at, kr, level)
    cursor.execute(query, values)
    db.commit()


root = tk.Tk()
root.title("Розрахунок kr")

object_label = tk.Label(root, text="Назва об'єкта:")
object_label.pack()
object_combobox = ttk.Combobox(root, values=[obj.value for obj in ObjectName], state="readonly")
object_combobox.pack()
pollutant_label = tk.Label(root, text="Тип субстанції:")
pollutant_label.pack()
pollutant_combobox = ttk.Combobox(root, values=[poll.value for poll in PollutantName], state="readonly")
pollutant_combobox.pack()

input_labels = ["Концентрація речовини в атмосферному повітрі, мг/куб.м", "Концентрація речовини у повітрі приміщення, мг/куб.м", "Час, що проводиться поза приміщенням, год/доба", "Час, що проводиться у приміщенні, год/доба", "Швидкість дихання поза приміщенням, куб.м/год", "Швидкість дихання у приміщенні, куб.м/год", "Частота впливу, днів/рік", "Тривалість впливу, років", "Маса тіла, кг", "Період осереднення експозиції, років"]

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

calculate_button = tk.Button(root, text="Розрахувати kr", command=calculate_kr)
calculate_button.pack()
kr_result = tk.Label(root, text="")
kr_result.pack()

def show_history():
    cursor.execute("SELECT * FROM data_calculations_kr")
    data = cursor.fetchall()

    history_window = tk.Toplevel(root)
    history_window.title("Історія")

    def display_data_calculations_kr():
        treeview.delete(*treeview.get_children())

        cursor.execute("SELECT * FROM data_calculations_kr")
        data = cursor.fetchall()

        for row in data:
            treeview.insert("", "end", values=row)

    treeview = ttk.Treeview(history_window, columns=("ID","Object Name", "Pollutant Name", "ca", "ch", "tout", "tin", "vout", "vin", "ef", "ed", "bw", "at", "kr", "level"))
    treeview.heading("#1", text="ID" ,anchor="w")
    treeview.heading("#2", text="Назва об'єкту",anchor="w")
    treeview.heading("#3", text="Назва субстанції",anchor="w")
    treeview.heading("#4", text="Концентрація речовини в атмосферному повітрі, мг/куб.м",anchor="w")
    treeview.heading("#5", text="Концентрація речовини у повітрі приміщення, мг/куб.м",anchor="w")
    treeview.heading("#6", text="Час, що проводиться поза приміщенням, год/доба",anchor="w")
    treeview.heading("#7", text="Час, що проводиться у приміщенні, год/доба",anchor="w")
    treeview.heading("#8", text="Швидкість дихання поза приміщенням, куб.м/год",anchor="w")
    treeview.heading("#9", text="Швидкість дихання у приміщенні, куб.м/год",anchor="w")
    treeview.heading("#10", text="Частота впливу, днів/рік",anchor="w")
    treeview.heading("#11", text="Тривалість впливу, років",anchor="w")
    treeview.heading("#12", text="Маса тіла, кг",anchor="w")
    treeview.heading("#13", text="Період осереднення експозиції, років",anchor="w")
    treeview.heading("#14", text="LADD",anchor="w")
    treeview.heading("#15", text="Рівень Небезпеки",anchor="w")
    treeview.column("#0", width=0)
    treeview.column("#1", width=10)
    treeview.column("#3", width=100)
    treeview.column("#4", width=60)
    treeview.column("#5", width=60)
    treeview.column("#6", width=60)
    treeview.column("#7", width=60)
    treeview.column("#8", width=60)
    treeview.column("#9", width=60)
    treeview.column("#10", width=60)
    treeview.column("#11", width=60)
    treeview.column("#12", width=60)
    treeview.column("#13", width=60)

    treeview.pack()

    for row in data:
        treeview.insert("", "end", values=row)

    treeview.pack()

history_button = tk.Button(root, text="Історія", command=show_history)
history_button.pack()

root.mainloop()
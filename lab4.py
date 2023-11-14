import tkinter as tk
from tkinter import ttk
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1809",
    database="ecomon"
)

cursor = db.cursor()


root = tk.Tk()
root.title("Автоматичний калькулятор податків")

object_label = tk.Label(root, text="Оберіть об'єкт:")
object_label.pack()


cursor.execute("SELECT DISTINCT objectName FROM data")
object_names = [row[0] for row in cursor.fetchall()]

object_combobox = ttk.Combobox(root, values=object_names, state="readonly")
object_combobox.pack()

year_label = tk.Label(root, text="Оберіть рік:")
year_label.pack()


cursor.execute("SELECT DISTINCT year FROM data")
years = [row[0] for row in cursor.fetchall()]

year_combobox = ttk.Combobox(root, values=years, state="readonly")
year_combobox.pack()


result_var = tk.StringVar()

def calculate_taxes():
    object_name = object_combobox.get()
    year = year_combobox.get()

    cursor.execute("SELECT * FROM data WHERE objectName = %s AND year = %s", (object_name, year))
    data_row = cursor.fetchone()

    if data_row:

        no2, so2, co, microparts = data_row[4:8]

        cursor.execute("SELECT * FROM taxes")
        tax_data = cursor.fetchall()


        if len(tax_data) >= 4:
            tax_amount = {
                'NO2': no2 * tax_data[1][2],
                'SO2': so2 * tax_data[2][2],
                'CO': co * tax_data[3][2],
                'Тверді речовини': microparts * tax_data[4][2]
            }

            query = "INSERT INTO taxes_payment (year, objectName, no2, so2, co, microparts, summary) " \
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (year, object_name, tax_amount['NO2'], tax_amount['SO2'], tax_amount['CO'],
                      tax_amount['Тверді речовини'], sum(tax_amount.values()))
            cursor.execute(query, values)
            db.commit()

            result_var.set(f"Розраховані та збережені податки для {object_name} становлять {sum(tax_amount.values())} грн. в {year} році")
        else:
            result_var.set("Помилка: недостатньо рядків у таблиці taxes.")
    else:
        result_var.set(f"Даних про викиди не знайдено для {object_name} у  {year} році")

def show_history():
    cursor.execute("SELECT year, objectName, no2, so2, co, microparts, summary FROM taxes_payment")
    data = cursor.fetchall()

    history_window = tk.Toplevel(root)
    history_window.title("Tax Payment History")

    treeview = ttk.Treeview(history_window, columns=("Year", "Object Name","NO2", "SO2", "CO", "Microparts", "Summary"))
    treeview.heading("#1", text="Year", anchor="w")
    treeview.heading("#2", text="Object Name", anchor="w")
    treeview.heading("#3", text="NO2", anchor="w")
    treeview.heading("#4", text="SO2", anchor="w")
    treeview.heading("#5", text="CO", anchor="w")
    treeview.heading("#6", text="Microparts", anchor="w")
    treeview.heading("#7", text="Summary", anchor="w")

    treeview.pack()

    for row in data:
        treeview.insert("", "end", values=row)

calculate_button = tk.Button(root, text="Розрахувати податки", command=calculate_taxes)
calculate_button.pack()

history_button = tk.Button(root, text="Історія", command=show_history)
history_button.pack()


summary_label = tk.Label(root, text="Сума податків:")
summary_label.pack()

summary_result_label = tk.Label(root, textvariable=result_var)
summary_result_label.pack()

root.mainloop()

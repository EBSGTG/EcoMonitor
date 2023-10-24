import mysql.connector
from tkinter import *
from tkinter import ttk

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1809",
    database="ecomon"
)

cursor = db_connection.cursor()

def calculate_and_save_nkr():
    object_name = object_name_var.get()
    substance_name = substance_name_var.get()
    concentration = concentration_var.get()

    cursor.execute("SELECT rfc_n FROM rfc WHERE substanceName = %s", (substance_name,))
    rfc_value = cursor.fetchone()[0]

    nkr = concentration / float(rfc_value)

    cursor.execute(
        "INSERT INTO data_calculations_nkr (objectName, substanceName, concentration, nkr) VALUES (%s, %s, %s, %s)",
        (object_name, substance_name, concentration, nkr))
    db_connection.commit()

    nkr_label.config(text=f"nkr = {nkr}")

    if nkr > 1:
        color = 'red'
    elif nkr == 1:
        color = '#D49B54'
    else:
        color = 'green'

    nkr_label.config(fg=color)

def show_history():
    cursor.execute("SELECT objectName, substanceName, concentration, nkr FROM data_calculations_nkr")
    data = cursor.fetchall()

    history_window = Toplevel(root)
    history_window.title("Історія")

    tree = ttk.Treeview(history_window, columns=("objectName", "substanceName", "concentration", "nkr"), show="headings")
    tree.heading("objectName", text="Об'єкт")
    tree.heading("substanceName", text="Речовина")
    tree.heading("concentration", text="Концентрація")
    tree.heading("nkr", text="Критерії неканцерогенного ризику")

    for row in data:
        tree.insert("", "end", values=row)

    tree.pack()

root = Tk()
root.title("Калькулятор NKR")

object_name_label = Label(root, text="Об'єкт:")
object_name_label.pack()
object_name_var = StringVar()
object_name_var.set("ТзОВ «Птахокомплекс Губин»")
object_name_menu = OptionMenu(root, object_name_var, 'ТзОВ «Птахокомплекс Губин»',
                              'Локачинський ЦВНТК ПАТ «Укrgазвидобування»', 'ДП «Волиньторф»')
object_name_menu.pack()

substance_name_label = Label(root, text="Речовина:")
substance_name_label.pack()
substance_name_var = StringVar()
substance_name_var.set("NO2")
substance_name_menu = OptionMenu(root, substance_name_var, 'NO2', 'SO2', 'CO')
substance_name_menu.pack()

concentration_label = Label(root, text="Концентрація:")
concentration_label.pack()
concentration_var = DoubleVar()
concentration_entry = Entry(root, textvariable=concentration_var)
concentration_entry.pack()

calculate_button = Button(root, text="Обчислити та Зберегти", command=calculate_and_save_nkr)
calculate_button.pack()
nkr_label = Label(root, text="", fg="black")
nkr_label.pack()
history_button = Button(root, text="Історія", command=show_history)
history_button.pack()
root.mainloop()
cursor.close()
db_connection.close()
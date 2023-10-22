import mysql.connector
from tkinter import *
from tkinter import ttk

# Підключення до бази даних
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2004",
    database="ecomon"
)

# Створення об'єкту курсора
cursor = db_connection.cursor()


# Функція для вирахування nkr та збереження в базі даних
def calculate_and_save_nkr():
    object_name = object_name_var.get()
    substance_name = substance_name_var.get()
    concentration = concentration_var.get()

    # Отримати RFC за певною речовиною
    cursor.execute("SELECT rfc_n FROM rfc WHERE substanceName = %s", (substance_name,))
    rfc_value = cursor.fetchone()[0]

    # Розрахунок nkr
    nkr = concentration / float(rfc_value)

    # Збереження nkr в базі даних
    cursor.execute(
        "INSERT INTO data_calculations_nkr (objectName, substanceName, concentration, nkr) VALUES (%s, %s, %s, %s)",
        (object_name, substance_name, concentration, nkr))
    db_connection.commit()

    # Вивести kr
    nkr_label.config(text=f"nkr = {nkr}")

    # Встановити колір тексту мітки в залежності від значення nkr
    if nkr > 1:
        color = 'red'
    elif nkr == 1:
        color = '#D49B54'
    else:
        color = 'green'

    nkr_label.config(fg=color)


# Функція для виведення таблиці історії
def show_history():
    cursor.execute("SELECT objectName, substanceName, concentration, nkr FROM data_calculations_nkr")
    data = cursor.fetchall()

    # Створити нове вікно для відображення таблиці
    history_window = Toplevel(root)
    history_window.title("Історія")

    # Створити та налаштувати таблицю
    tree = ttk.Treeview(history_window, columns=("objectName", "substanceName", "concentration", "nkr"), show="headings")
    tree.heading("objectName", text="Об'єкт")
    tree.heading("substanceName", text="Речовина")
    tree.heading("concentration", text="Концентрація")
    tree.heading("nkr", text="Критерії неканцерогенного ризику")

    for row in data:
        tree.insert("", "end", values=row)

    tree.pack()


# Створення графічного інтерфейсу
root = Tk()
root.title("Калькулятор NKR")

object_name_label = Label(root, text="Об'єкт:")
object_name_label.pack()
object_name_var = StringVar()
object_name_var.set("ТзОВ «Птахокомплекс Губин»")  # Значення за замовчуванням
object_name_menu = OptionMenu(root, object_name_var, 'ТзОВ «Птахокомплекс Губин»',
                              'Локачинський ЦВНТК ПАТ «Укrgазвидобування»', 'ДП «Волиньторф»')
object_name_menu.pack()

substance_name_label = Label(root, text="Речовина:")
substance_name_label.pack()
substance_name_var = StringVar()
substance_name_var.set("NO2")  # Значення за замовчуванням
substance_name_menu = OptionMenu(root, substance_name_var, 'NO2', 'SO2', 'CO')
substance_name_menu.pack()

concentration_label = Label(root, text="Концентрація:")
concentration_label.pack()
concentration_var = DoubleVar()
concentration_entry = Entry(root, textvariable=concentration_var)
concentration_entry.pack()

calculate_button = Button(root, text="Обчислити та Зберегти", command=calculate_and_save_nkr)
calculate_button.pack()

# Мітка для виведення nkr
nkr_label = Label(root, text="", fg="black")
nkr_label.pack()

# Кнопка для виведення таблиці історії
history_button = Button(root, text="Історія", command=show_history)
history_button.pack()

root.mainloop()

# Завершення з'єднання з базою даних
cursor.close()
db_connection.close()

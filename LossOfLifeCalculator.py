import tkinter as tk
from tkinter import ttk
import mysql.connector


def calculate_losses():
    try:
        ml = float(entry_ml.get())
        mt = float(entry_mt.get())
        mi = float(entry_mi.get())
        mz_adult = float(entry_mz_adult.get())
        mz_child = float(entry_mz_child.get())

        num_l = int(entry_num_l.get())
        num_t = int(entry_num_t.get())
        num_i = int(entry_num_i.get())
        num_z_adult = int(entry_num_z_adult.get())
        num_z_child = int(entry_num_z_child.get())

        loss_rr = ml * num_l + mt * num_t + mi * num_i + mz_adult * num_z_adult + mz_child * num_z_child

        label_result.config(text=f"Розмір збитків: {loss_rr} тис. гривень")

        # Підключення до бази даних
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2004",
            database="ecomon"
        )

        cursor = connection.cursor()

        # Вставка результату обрахунків до таблиці
        insert_query = "INSERT INTO LossOfLife (ml, mt, mi, mz_adult, mz_child, num_l, num_t, num_i, num_z_adult, num_z_child, loss_rr) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (ml, mt, mi, mz_adult, mz_child, num_l, num_t, num_i, num_z_adult, num_z_child, loss_rr)

        cursor.execute(insert_query, values)

        # Підтвердження та закриття з'єднання
        connection.commit()
        connection.close()

    except ValueError:
        label_result.config(text="Будь ласка, введіть числа.")
    except mysql.connector.Error as error:
        print("Помилка підключення до бази даних:", error)

def show_history():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2004",
            database="ecomon"
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM LossOfLife")
        data = cursor.fetchall()

        history_window = tk.Toplevel(root)
        history_window.title("Історія LossOfLife")

        treeview = ttk.Treeview(history_window, columns=(
            "ID", "Легкий випадок", "Тяжкий випадок", "Втрати від інвалідності", "Загибель дорослої людини", "Загибель дитини", "Кількість постраждалих від легкого випадку", "Кількість постраждалих від тяжкого випадку", "Кількість постраждалих від інвалідності", "Кількість загиблих дорослих", "Кількість загиблих дітей", "Сума збитків"
        ))

        for index, col in enumerate(
                ["ID", "Легкий випадок", "Тяжкий випадок", "Втрати від інвалідності", "Загибель дорослої людини",
                 "Загибель дитини", "Кількість постраждалих від легкого випадку",
                 "Кількість постраждалих від тяжкого випадку", "Кількість постраждалих від інвалідності",
                 "Кількість загиблих дорослих", "Кількість загиблих дітей", "Сума збитків"]):
            treeview.heading(f"#{index}", text=col)
            treeview.column(f"#{index}", width=50)

        for row in data:
            treeview.insert("", "end", values=row)

        treeview.pack(fill='both', expand=True)

    except mysql.connector.Error as error:
        print("Помилка підключення до бази даних:", error)



root = tk.Tk()
root.title("Розрахунок збитків")

# Написи та поля для введення даних
entries = [
    "Легкий нещасний випадок (Мл):",
    "Тяжкий нещасний випадок (Мт):",
    "Втрати від інвалідності (Мі):",
    "Загибель дорослої людини (Мз, дорослий):",
    "Загибель дитини (Мз, дитина):",
    "Кількість постраждалих від легкого нещасного випадку:",
    "Кількість постраждалих від тяжкого нещасного випадку:",
    "Кількість постраждалих від інвалідності:",
    "Кількість загиблих дорослих:",
    "Кількість загиблих дітей:"
]

entries_label = tk.Label(root, text="Введіть значення:")
entries_label.pack()

entry_labels = []
entry_inputs = []

for entry_text in entries:
    label = tk.Label(root, text=entry_text)
    entry_labels.append(label)
    label.pack()

    entry = tk.Entry(root)
    entry_inputs.append(entry)
    entry.pack()

# Кнопка для розрахунку
calculate_button = tk.Button(root, text="Обчислити збитки", command=calculate_losses)
calculate_button.pack()

history_button = tk.Button(root, text="Історія", command=show_history)
history_button.pack()

# Виведення результату
label_result = tk.Label(root, text="")
label_result.pack()

# Оновлення змінних для доступу до полів вводу за допомогою індексів
entry_ml = entry_inputs[0]
entry_mt = entry_inputs[1]
entry_mi = entry_inputs[2]
entry_mz_adult = entry_inputs[3]
entry_mz_child = entry_inputs[4]
entry_num_l = entry_inputs[5]
entry_num_t = entry_inputs[6]
entry_num_i = entry_inputs[7]
entry_num_z_adult = entry_inputs[8]
entry_num_z_child = entry_inputs[9]

root.mainloop()

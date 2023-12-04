import tkinter as tk

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
    except ValueError:
        label_result.config(text="Будь ласка, введіть числа.")


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

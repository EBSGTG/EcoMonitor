import tkinter as tk

def calculate_losses_Fv():
    def calculate_losses():
        # Отримання значень з полів вводу
        delta_R = float(entry_delta_R.get())
        K = float(entry_K.get())
        n = int(entry_n.get())
        Lv = float(entry_Lv.get())

        # Розрахунок збитків від руйнування та пошкодження основних фондів
        losses = 0
        for i in range(1, n + 1):
            losses += (delta_R * K) - Lv

        # Відображення результату
        label_result.config(text=f"Total Losses: {losses}")

    # Створення головного вікна
    root = tk.Tk()
    root.title("Розрахунок збитків")

    # Створення текстових міток та полів для введення значень змінних для формули розрахунку збитків
    label_delta_R = tk.Label(root, text="Введіть значення delta_R:")
    label_delta_R.pack()

    entry_delta_R = tk.Entry(root)
    entry_delta_R.pack()

    label_K = tk.Label(root, text="Введіть значення К:")
    label_K.pack()

    entry_K = tk.Entry(root)
    entry_K.pack()

    label_n = tk.Label(root, text="Введіть кількість видів основних фондів:")
    label_n.pack()

    entry_n = tk.Entry(root)
    entry_n.pack()

    label_Lv = tk.Label(root, text="Введіть значення Лv:")
    label_Lv.pack()

    entry_Lv = tk.Entry(root)
    entry_Lv.pack()

    # Створення кнопки для розрахунку збитків
    button_calculate = tk.Button(root, text="Calculate Losses", command=calculate_losses)
    button_calculate.pack()

    # Label для відображення результату
    label_result = tk.Label(root)
    label_result.pack()

    # Запуск головного циклу обробки подій
    root.mainloop()


def calculate_losses_Fg():
    # Розрахунок збитків від руйнування основних фондів невиробничого призначення
    return 0


def calculate_losses_Pr():
    # Розрахунок збитків від втрат готової промислової продукції
    return 0


def calculate_losses_Prs():
    # Розрахунок збитків від втрат незібраної сільськогосподарської продукції
    return 0


def calculate_losses_Sn():
    # Розрахунок збитків від втрат запасів сировини, напівфабрикатів та проміжної продукції
    return 0


def calculate_losses_Mdg():
    # Розрахунок збитків від втрат майна громадян та організацій
    return 0


# Функція для підсумкового розрахунку суми всіх збитків
# Функція для підсумкового розрахунку суми всіх збитків
def calculate_total_losses():
    total_losses = 0
    total_losses += calculate_losses_Fv()
    total_losses += calculate_losses_Fg()
    total_losses += calculate_losses_Pr()
    total_losses += calculate_losses_Prs()
    total_losses += calculate_losses_Sn()
    total_losses += calculate_losses_Mdg()
    label_total_losses.config(text=f"Total Losses: {total_losses}")

root = tk.Tk()
root.title("Розрахунок збитків")

labels_text = ["Fv: 0", "Fg: 0", "Pr: 0", "Prs: 0", "Sn: 0", "Mdg: 0"]
buttons_text = ["Calculate Fv", "Calculate Fg", "Calculate Pr", "Calculate Prs", "Calculate Sn", "Calculate Mdg"]

labels = [tk.Label(root, text=text) for text in labels_text]
for label in labels:
    label.pack()

buttons = [tk.Button(root, text=text) for text in buttons_text]
for button in buttons:
    button.pack()

button_total_losses = tk.Button(root, text="Calculate Total Losses", command=calculate_total_losses)
button_total_losses.pack()

label_total_losses = tk.Label(root)
label_total_losses.pack()

root.mainloop()
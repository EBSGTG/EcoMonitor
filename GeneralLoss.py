import tkinter as tk

LossOfProductionFunds = 0
NonProductionFundsLoss = 0
LossOfFinishedIndustrialProduct = 0
LossOfUnfinishedIndustrialProduct = 0
LossOfMaterials = 0
OtherPropertyLoss = 0


def func1():
    def calculate_losses():
        global LossOfProductionFunds
        try:
            delta_rs = [float(entry_delta_r1.get()), float(entry_delta_r2.get()), float(entry_delta_r3.get())]
            ks = [float(entry_k1.get()), float(entry_k2.get()), float(entry_k3.get())]
            lv = float(entry_lv.get())

            total_loss = sum([(delta_rs[i] * ks[i]) for i in range(len(delta_rs))]) - lv
            LossOfProductionFunds = total_loss

            label_result.config(text=f"Загальні збитки: {total_loss} гривень")
        except ValueError:
            label_result.config(text="Будь ласка, введіть числа.")



    root = tk.Tk()
    root.title("Розрахунок загальних збитків")

    entries = [
        "Балансова вартість 1-го фонду:",
        "Балансова вартість 2-го фонду:",
        "Балансова вартість 3-го фонду:",
        "Коефіцієнт амортизації 1-го фонду:",
        "Коефіцієнт амортизації 2-го фонду:",
        "Коефіцієнт амортизації 3-го фонду:",
        "Ліквідаційна вартість:"
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

    calculate_button = tk.Button(root, text="Обчислити збитки", command=calculate_losses)
    calculate_button.pack()

    label_result = tk.Label(root, text="")
    label_result.pack()

    entry_delta_r1 = entry_inputs[0]
    entry_delta_r2 = entry_inputs[1]
    entry_delta_r3 = entry_inputs[2]
    entry_k1 = entry_inputs[3]
    entry_k2 = entry_inputs[4]
    entry_k3 = entry_inputs[5]
    entry_lv = entry_inputs[6]

    root.mainloop()





def func2():
    def calculate_losses():
        global NonProductionFundsLoss
        try:
            delta_rs = [float(entry_delta_r1.get()), float(entry_delta_r2.get()), float(entry_delta_r3.get())]
            ks = [float(entry_k1.get()), float(entry_k2.get()), float(entry_k3.get())]
            lv = float(entry_lv.get())

            total_loss = sum([(delta_rs[i] * ks[i]) for i in range(len(delta_rs))]) - lv
            NonProductionFundsLoss = total_loss

            label_result.config(text=f"Загальні збитки: {total_loss} гривень")
        except ValueError:
            label_result.config(text="Будь ласка, введіть числа.")

    root = tk.Tk()
    root.title("Розрахунок загальних збитків")

    entries = [
        "Балансова вартість 1-го фонду:",
        "Балансова вартість 2-го фонду:",
        "Балансова вартість 3-го фонду:",
        "Коефіцієнт амортизації 1-го фонду:",
        "Коефіцієнт амортизації 2-го фонду:",
        "Коефіцієнт амортизації 3-го фонду:",
        "Ліквідаційна вартість:"
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

    calculate_button = tk.Button(root, text="Обчислити збитки", command=calculate_losses)
    calculate_button.pack()

    label_result = tk.Label(root, text="")
    label_result.pack()

    entry_delta_r1 = entry_inputs[0]
    entry_delta_r2 = entry_inputs[1]
    entry_delta_r3 = entry_inputs[2]
    entry_k1 = entry_inputs[3]
    entry_k2 = entry_inputs[4]
    entry_k3 = entry_inputs[5]
    entry_lv = entry_inputs[6]

    root.mainloop()

def func3():
    def calculate_losses():
        global LossOfFinishedIndustrialProduct
        try:
            unit_costs = [float(entry_cost1.get()), float(entry_cost2.get()), float(entry_cost3.get())]
            quantities = [int(entry_quantity1.get()), int(entry_quantity2.get()), int(entry_quantity3.get())]
            total_loss = sum([(unit_costs[i] * quantities[i]) for i in range(len(unit_costs))])

            LossOfFinishedIndustrialProduct = total_loss

            label_result.config(text=f"Загальні збитки: {total_loss} гривень")
        except ValueError:
            label_result.config(text="Будь ласка, введіть числа.")

    root = tk.Tk()
    root.title("Розрахунок збитків від втрат продукції")

    entries = [
        "Собівартість продукції 1:",
        "Собівартість продукції 2:",
        "Собівартість продукції 3:",
        "Кількість втраченої продукції 1:",
        "Кількість втраченої продукції 2:",
        "Кількість втраченої продукції 3:"
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

    calculate_button = tk.Button(root, text="Обчислити збитки", command=calculate_losses)
    calculate_button.pack()

    label_result = tk.Label(root, text="")
    label_result.pack()

    entry_cost1 = entry_inputs[0]
    entry_cost2 = entry_inputs[1]
    entry_cost3 = entry_inputs[2]
    entry_quantity1 = entry_inputs[3]
    entry_quantity2 = entry_inputs[4]
    entry_quantity3 = entry_inputs[5]

    root.mainloop()

def func4():
    def calculate_losses():
        global LossOfUnfinishedIndustrialProduct
        try:
            areas = [float(entry_area1.get()), float(entry_area2.get()), float(entry_area3.get())]
            damage_coefficients = [float(entry_damage_coeff1.get()), float(entry_damage_coeff2.get()),
                                   float(entry_damage_coeff3.get())]
            expected_yields = [float(entry_expected_yield1.get()), float(entry_expected_yield2.get()),
                               float(entry_expected_yield3.get())]
            wholesale_prices = [float(entry_wholesale_price1.get()), float(entry_wholesale_price2.get()),
                                float(entry_wholesale_price3.get())]
            additional_costs = [float(entry_additional_cost1.get()), float(entry_additional_cost2.get()),
                                float(entry_additional_cost3.get())]

            total_loss = sum(
                [(areas[i] * damage_coefficients[i] * expected_yields[i] * wholesale_prices[i] - additional_costs[i])
                 for i in range(len(areas))])
            LossOfUnfinishedIndustrialProduct = total_loss

            label_result.config(text=f"Збитки від незібраної продукції: {total_loss} гривень")
        except ValueError:
            label_result.config(text="Будь ласка, введіть числа.")

    root = tk.Tk()
    root.title("Розрахунок збитків від незібраної сільськогосподарської продукції")

    entries = [
        "Площа пошкодження 1-ї культури:",
        "Площа пошкодження 2-ї культури:",
        "Площа пошкодження 3-ї культури:",
        "Коефіцієнт пошкодження 1-ї культури:",
        "Коефіцієнт пошкодження 2-ї культури:",
        "Коефіцієнт пошкодження 3-ї культури:",
        "Прогнозована урожайність 1-ї культури:",
        "Прогнозована урожайність 2-ї культури:",
        "Прогнозована урожайність 3-ї культури:",
        "Прогнозована оптова ціна 1-ї культури:",
        "Прогнозована оптова ціна 2-ї культури:",
        "Прогнозована оптова ціна 3-ї культури:",
        "Додаткові витрати на 1-у культуру:",
        "Додаткові витрати на 2-у культуру:",
        "Додаткові витрати на 3-ю культуру:"
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

    calculate_button = tk.Button(root, text="Обчислити збитки", command=calculate_losses)
    calculate_button.pack()

    label_result = tk.Label(root, text="")
    label_result.pack()

    entry_area1 = entry_inputs[0]
    entry_area2 = entry_inputs[1]
    entry_area3 = entry_inputs[2]
    entry_damage_coeff1 = entry_inputs[3]
    entry_damage_coeff2 = entry_inputs[4]
    entry_damage_coeff3 = entry_inputs[5]
    entry_expected_yield1 = entry_inputs[6]
    entry_expected_yield2 = entry_inputs[7]
    entry_expected_yield3 = entry_inputs[8]
    entry_wholesale_price1 = entry_inputs[9]
    entry_wholesale_price2 = entry_inputs[10]
    entry_wholesale_price3 = entry_inputs[11]
    entry_additional_cost1 = entry_inputs[12]
    entry_additional_cost2 = entry_inputs[13]
    entry_additional_cost3 = entry_inputs[14]

    root.mainloop()

def func5():
    def calculate_losses():
        global LossOfMaterials
        try:
            wholesale_prices = [float(entry_wholesale_price1.get()), float(entry_wholesale_price2.get()),
                                float(entry_wholesale_price3.get())]
            quantities = [int(entry_quantity1.get()), int(entry_quantity2.get()), int(entry_quantity3.get())]

            total_loss = sum([(wholesale_prices[i] * quantities[i]) for i in range(len(wholesale_prices))])
            LossOfMaterials = total_loss

            label_result.config(text=f"Збитки від втрат сировини: {total_loss} гривень")
        except ValueError:
            label_result.config(text="Будь ласка, введіть числа.")

    root = tk.Tk()
    root.title("Розрахунок збитків від втрат сировини")

    entries = [
        "Середня оптова ціна сировини/матеріалу 1:",
        "Середня оптова ціна сировини/матеріалу 2:",
        "Середня оптова ціна сировини/матеріалу 3:",
        "Обсяг втраченої сировини/матеріалу 1:",
        "Обсяг втраченої сировини/матеріалу 2:",
        "Обсяг втраченої сировини/матеріалу 3:"
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

    calculate_button = tk.Button(root, text="Обчислити збитки", command=calculate_losses)
    calculate_button.pack()

    label_result = tk.Label(root, text="")
    label_result.pack()

    entry_wholesale_price1 = entry_inputs[0]
    entry_wholesale_price2 = entry_inputs[1]
    entry_wholesale_price3 = entry_inputs[2]
    entry_quantity1 = entry_inputs[3]
    entry_quantity2 = entry_inputs[4]
    entry_quantity3 = entry_inputs[5]

    root.mainloop()

def func6():
    def calculate_losses():
        global OtherPropertyLoss
        try:
            # Для організацій
            org_assets = [float(entry_org_asset1.get()), float(entry_org_asset2.get()), float(entry_org_asset3.get())]
            org_depreciation = [float(entry_org_depreciation1.get()), float(entry_org_depreciation2.get()),
                                float(entry_org_depreciation3.get())]
            org_price_indices = [float(entry_org_price_index1.get()), float(entry_org_price_index2.get()),
                                 float(entry_org_price_index3.get())]
            org_quantities = [int(entry_org_quantity1.get()), int(entry_org_quantity2.get()),
                              int(entry_org_quantity3.get())]

            # Для громадян
            market_prices = [float(entry_market_price1.get()), float(entry_market_price2.get()),
                             float(entry_market_price3.get())]
            citizen_quantities = [int(entry_citizen_quantity1.get()), int(entry_citizen_quantity2.get()),
                                  int(entry_citizen_quantity3.get())]

            # Розрахунок збитків
            org_loss = sum([(org_assets[i] * org_depreciation[i] * org_price_indices[i] * org_quantities[i]) for i in
                            range(len(org_assets))])
            citizen_loss = sum([(market_prices[i] * citizen_quantities[i]) for i in range(len(market_prices))])

            total_loss = org_loss + citizen_loss

            OtherPropertyLoss = total_loss
            label_result.config(text=f"Збитки від втрат майна: {total_loss} гривень")
        except ValueError:
            label_result.config(text="Будь ласка, введіть числа.")

    root = tk.Tk()
    root.title("Розрахунок збитків від втрат майна")

    entries_org = [
        "Балансова вартість майна організації 1:",
        "Балансова вартість майна організації 2:",
        "Балансова вартість майна організації 3:",
        "Коефіцієнт амортизації майна організації 1:",
        "Коефіцієнт амортизації майна організації 2:",
        "Коефіцієнт амортизації майна організації 3:",
        "Індекс зміни цін майна організації 1:",
        "Індекс зміни цін майна організації 2:",
        "Індекс зміни цін майна організації 3:",
        "Кількість втраченого майна організації 1:",
        "Кількість втраченого майна організації 2:",
        "Кількість втраченого майна організації 3:"
    ]

    entries_citizen = [
        "Середня ринкова ціна майна громадян 1:",
        "Середня ринкова ціна майна громадян 2:",
        "Середня ринкова ціна майна громадян 3:",
        "Кількість втраченого майна громадян 1:",
        "Кількість втраченого майна громадян 2:",
        "Кількість втраченого майна громадян 3:"
    ]

    org_entries_label = tk.Label(root, text="Введіть дані для організацій:")
    org_entries_label.pack()

    citizen_entries_label = tk.Label(root, text="Введіть дані для громадян:")
    citizen_entries_label.pack()

    entry_labels = []
    entry_inputs = []

    for entry_text in entries_org:
        label = tk.Label(root, text=entry_text)
        entry_labels.append(label)
        label.pack()

        entry = tk.Entry(root)
        entry_inputs.append(entry)
        entry.pack()

    for entry_text in entries_citizen:
        label = tk.Label(root, text=entry_text)
        entry_labels.append(label)
        label.pack()

        entry = tk.Entry(root)
        entry_inputs.append(entry)
        entry.pack()

    calculate_button = tk.Button(root, text="Обчислити збитки", command=calculate_losses)
    calculate_button.pack()

    label_result = tk.Label(root, text="")
    label_result.pack()

    entry_org_asset1 = entry_inputs[0]
    entry_org_asset2 = entry_inputs[1]
    entry_org_asset3 = entry_inputs[2]
    entry_org_depreciation1 = entry_inputs[3]
    entry_org_depreciation2 = entry_inputs[4]
    entry_org_depreciation3 = entry_inputs[5]
    entry_org_price_index1 = entry_inputs[6]
    entry_org_price_index2 = entry_inputs[7]
    entry_org_price_index3 = entry_inputs[8]
    entry_org_quantity1 = entry_inputs[9]
    entry_org_quantity2 = entry_inputs[10]
    entry_org_quantity3 = entry_inputs[11]

    entry_market_price1 = entry_inputs[12]
    entry_market_price2 = entry_inputs[13]
    entry_market_price3 = entry_inputs[14]
    entry_citizen_quantity1 = entry_inputs[15]
    entry_citizen_quantity2 = entry_inputs[16]
    entry_citizen_quantity3 = entry_inputs[17]

    root.mainloop()

def update_values():
    global LossOfProductionFunds
    global NonProductionFundsLoss
    global LossOfFinishedIndustrialProduct
    global LossOfUnfinishedIndustrialProduct
    global LossOfMaterials
    global OtherPropertyLoss
    values = [LossOfProductionFunds, NonProductionFundsLoss, LossOfFinishedIndustrialProduct, LossOfUnfinishedIndustrialProduct, LossOfMaterials, OtherPropertyLoss]
    label_func1.config(text=f"func1: {values[0]:>5}")
    label_func2.config(text=f"func2: {values[1]:>5}")
    label_func3.config(text=f"func3: {values[2]:>5}")
    label_func4.config(text=f"func4: {values[3]:>5}")
    label_func5.config(text=f"func5: {values[4]:>5}")
    label_func6.config(text=f"func6: {values[5]:>5}")
    label_sum.config(text=f"Сума: {sum(values):>5}")

root = tk.Tk()
root.title("Обчислення функцій")



label_func1 = tk.Label(root, text="func1: ")
label_func1.pack()
button_func1 = tk.Button(root, text="Функція 1", command=func1)
button_func1.pack()


label_func2 = tk.Label(root, text="func2: ")
label_func2.pack()
button_func2 = tk.Button(root, text="Функція 2", command=func2)
button_func2.pack()


label_func3 = tk.Label(root, text="func3: ")
label_func3.pack()
button_func3 = tk.Button(root, text="Функція 3", command=func3)
button_func3.pack()


label_func4 = tk.Label(root, text="func4: ")
label_func4.pack()
button_func4 = tk.Button(root, text="Функція 4", command=func4)
button_func4.pack()


label_func5 = tk.Label(root, text="func5: ")
label_func5.pack()
button_func5 = tk.Button(root, text="Функція 5", command=func5)
button_func5.pack()


label_func6 = tk.Label(root, text="func6: ")
label_func6.pack()
button_func6 = tk.Button(root, text="Функція 6", command=func6)
button_func6.pack()

label_sum = tk.Label(root, text="Сума: ")
label_sum.pack()


label_func7 = tk.Label(root, text="Обновити значення: ")
label_func7.pack()
button_func7 = tk.Button(root, text="Обновити", command=update_values)
button_func7.pack()

root.mainloop()

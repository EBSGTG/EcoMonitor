import mysql.connector
from tkinter import *
from tkinter import ttk
from enum import Enum

class ObjectName(Enum):
    PTAHOKOMPLEX_GUBIN = 'ТзОВ «Птахокомплекс Губин»'
    LOKACHYNSKIY_CVNTK = 'Локачинський ЦВНТК ПАТ «Укргазвидобування»'
    VOLYNTORF = 'ДП «Волиньторф»'
    FREE = 'FREE'

class Pollutant(Enum):
    AMMONIUM_NITRATE = 'Азот амонійний'
    ORGANIC_SUBSTANCES = 'Органічні речовини (БСК 5)'
    SUSPENDED_SUBSTANCES = 'Завислі речовини'
    OIL_PRODUCTS = 'Нафтопродукти'
    NITRATES = 'Нітрати'
    NITRITES = 'Нітрити'
    SULFATES = 'Сульфати'
    PHOSPHATES = 'Фосфати'
    CHLORIDES = 'Хлориди'
    OTHER = 'Інше'

class Concentration(Enum):
    UP_TO_0_001 = 'До 0,001 (включно)'
    FROM_0_001_TO_0_1 = 'Понад 0,001 - 0,1 (включно)'
    FROM_0_1_TO_1 = 'Понад 0,1 - 1 (включно)'
    FROM_1_TO_10 = 'Понад 1 - 10 (включно)'
    ABOVE_10 = 'Понад 10'
    OTHER = 'Обрано'

# Replace these values with your actual database connection details
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1809",
    database="ecomon"
)

class TaxCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Pollution Tax Calculator")

        self.year_label = Label(root, text="Рік:")
        self.year_label.pack()

        self.year_entry = Entry(root)
        self.year_entry.pack()

        self.object_label = Label(root, text="Назваа Об'єкта:")
        self.object_label.pack()

        self.object_var = StringVar()
        self.object_dropdown = OptionMenu(root, self.object_var, *[obj.value for obj in ObjectName])
        self.object_dropdown.pack()

        self.pollutant_label = Label(root, text="Забруднювач:")
        self.pollutant_label.pack()

        self.pollutant_var = StringVar()
        self.pollutant_dropdown = OptionMenu(root, self.pollutant_var, *[poll.value for poll in Pollutant])
        self.pollutant_dropdown.pack()

        self.concentration_label = Label(root, text="Концентрація:")
        self.concentration_label.pack()

        self.concentration_var = StringVar()
        self.concentration_dropdown = OptionMenu(root, self.concentration_var, *[conc.value for conc in Concentration])
        self.concentration_dropdown.pack()

        self.weight_label = Label(root, text="Вага (т):")
        self.weight_label.pack()

        self.weight_entry = Entry(root)
        self.weight_entry.pack()

        self.calculate_button = Button(root, text="Calculate Tax", command=self.calculate_tax)
        self.calculate_button.pack()

        self.result_label = Label(root, text="")
        self.result_label.pack()

        self.view_records_button = Button(root, text="View Records", command=self.view_records)
        self.view_records_button.pack()

    def calculate_tax(self):
        pollution = 1
        conc = 1
        year = int(self.year_entry.get())
        object_name = ObjectName(self.object_var.get())
        pollutant = Pollutant(self.pollutant_var.get())
        concentration = Concentration(self.concentration_var.get())
        weight = float(self.weight_entry.get())
        pollutant_name = pollutant.value
        concentration_value = concentration.value

        if pollutant_name == 'Азот амонійний':
            pollution = 12883.84
        elif pollutant_name == 'Органічні речовини (БСК 5)':
            pollution = 5156.8
        elif pollutant_name == 'Завислі речовини':
            pollution = 369.52
        elif pollutant_name == 'Нафтопродукти':
            pollution = 75792.4
        elif pollutant_name == 'Нітрати':
            pollution = 1108.56
        elif pollutant_name == 'Нітрити':
            pollution = 63278.16
        elif pollutant_name == 'Сульфати':
            pollution = 369.52
        elif pollutant_name == 'Фосфати':
            pollution = 10297.44
        elif pollutant_name == 'Хлориди':
            pollution = 369.52
        elif pollutant_name == 'Інше':
            pollution = 1.0

        if concentration_value == 'До 0,001 (включно)':
            conc = 1349948.0
        elif concentration_value == 'Понад 0,001 - 0,1 (включно)':
            conc = 978777.84
        elif concentration_value == 'Понад 0,1 - 1 (включно)':
            conc = 168741.52
        elif concentration_value == 'Понад 1 - 10 (включно)':
            conc = 17173.04
        elif concentration_value == 'Понад 10':
            conc = 3437.76
        elif concentration_value == 'Обрано':
            conc = 1.0


        tax = weight * conc * pollution

        # Display the calculated tax
        self.result_label.config(text=f"Calculated Tax: {tax}")

        # Save the data to the database
        self.save_to_database(year, object_name, pollutant_name, concentration_value, weight, tax)

    def save_to_database(self, year, object_name, pollutant_name, concentration, weight, tax):
        cursor = db.cursor()

        # Replace the table and column names with your actual database structure
        query = """
            INSERT INTO taxes_water (year, objectName, pollutant_name, concentration, weight, tax)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (year, object_name.value, pollutant_name, concentration, weight, tax)

        cursor.execute(query, values)
        db.commit()

        cursor.close()

    def view_records(self):
        records_window = Toplevel(self.root)
        records_window.title("Records from Database")

        tree = ttk.Treeview(records_window, columns=("ID", "Year", "Object Name", "Pollutant", "Concentration", "Weight", "Tax"))
        tree.heading("ID", text="ID")
        tree.heading("Year", text="Year")
        tree.heading("Object Name", text="Object Name")
        tree.heading("Pollutant", text="Pollutant")
        tree.heading("Concentration", text="Concentration")
        tree.heading("Weight", text="Weight")
        tree.heading("Tax", text="Tax")
        tree.pack()

        cursor = db.cursor()

        # Replace the table name with your actual database table name
        query = "SELECT * FROM taxes_water"

        cursor.execute(query)
        records = cursor.fetchall()

        # Display records in the Treeview
        for record in records:
            tree.insert("", "end", values=record)

        cursor.close()

if __name__ == "__main__":
    root = Tk()
    app = TaxCalculator(root)
    root.mainloop()

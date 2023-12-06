import mysql.connector
from tkinter import *
from tkinter import ttk
from enum import Enum

class DangerClass(Enum):
    I = 'надзвичайно небезпечні'
    II = 'високонебезпечні'
    III = 'помірно небезпечні'
    IV = 'малонебезпечні'
    V = 'малонебезпечні нетоксичні відходи гірничої промисловості'

class WasteZone(Enum):
    WITHIN_SETTLEMENT = 'В межах населеного пункту або на відстані менш як 3 км від таких меж'
    BEYOND_SETTLEMENT = 'На відстані від 3 км і більше від меж населеного пункту'

class ObjectName(Enum):
    PTAHOKOMPLEX_GUBIN = 'ТзОВ «Птахокомплекс Губин»'
    LOKACHYNSKIY_CVNTK = 'Локачинський ЦВНТК ПАТ «Укргазвидобування»'
    VOLYNTORF = 'ДП «Волиньторф»'
    FREE = 'FREE'

# Replace these values with your actual database connection details
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1809",
    database="ecomon"
)

class WasteTaxCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Waste Placement Tax Calculator")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=BOTH, expand=YES)

        # Tab for tax calculation
        self.calculation_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.calculation_tab, text="Calculate Tax")
        self.setup_calculation_tab()

        # Tab for viewing records
        self.records_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.records_tab, text="View Records")
        self.setup_records_tab()

    def setup_calculation_tab(self):
        Label(self.calculation_tab, text="Year:").pack()
        self.year_entry = Entry(self.calculation_tab)
        self.year_entry.pack()

        Label(self.calculation_tab, text="Object Name:").pack()
        self.object_var = StringVar(self.calculation_tab)
        self.object_var.set(ObjectName.PTAHOKOMPLEX_GUBIN.value)
        object_name_menu = OptionMenu(self.calculation_tab, self.object_var, *list(map(lambda x: x.value, ObjectName)))
        object_name_menu.pack()

        Label(self.calculation_tab, text="Weight (tons):").pack()
        self.weight_entry = Entry(self.calculation_tab)
        self.weight_entry.pack()

        Label(self.calculation_tab, text="Danger Class:").pack()
        self.danger_class_var = StringVar(self.calculation_tab)
        self.danger_class_var.set(DangerClass.I.value)
        danger_class_menu = OptionMenu(self.calculation_tab, self.danger_class_var, *list(map(lambda x: x.value, DangerClass)))
        danger_class_menu.pack()

        Label(self.calculation_tab, text="Waste Zone:").pack()
        self.waste_zone_var = StringVar(self.calculation_tab)
        self.waste_zone_var.set(WasteZone.WITHIN_SETTLEMENT.value)
        waste_zone_menu = OptionMenu(self.calculation_tab, self.waste_zone_var, *list(map(lambda x: x.value, WasteZone)))
        waste_zone_menu.pack()

        self.calculate_button = Button(self.calculation_tab, text="Calculate Tax", command=self.calculate_tax)
        self.calculate_button.pack()

        self.result_label = Label(self.calculation_tab, text="")
        self.result_label.pack()

    def setup_records_tab(self):
        # Add Treeview for displaying records
        self.setup_treeview()

        self.view_records_button = Button(self.records_tab, text="View Records", command=self.view_records)
        self.view_records_button.pack()

    def calculate_tax(self):
        v1 = 0.0
        v2 = 0.0
        year = int(self.year_entry.get())
        object_name = ObjectName(self.object_var.get())
        danger_class = DangerClass(self.danger_class_var.get())
        waste_zone = WasteZone(self.waste_zone_var.get())
        weight = float(self.weight_entry.get())


        class_danger = danger_class.value
        coef_danger = waste_zone.value

        if class_danger == 'надзвичайно небезпечні':
            v1 = 1546.22
        elif class_danger == 'високонебезпечні':
            v1 = 56.32
        elif class_danger == 'помірно небезпечні':
            v1 = 14.12
        elif class_danger == 'малонебезпечні':
            v1 = 5.50
        elif class_danger == 'малонебезпечні нетоксичні відходи гірничої промисловості':
            v1 = 0.54

        if coef_danger == 'В межах населеного пункту або на відстані менш як 3 км від таких меж':
            v2 = 3.0
        else:
            v2 = 1.0

        tax = weight * v1 * v2
        self.result_label.config(text=f"Calculated Tax: {tax}")
        self.save_to_database(year, object_name.value, class_danger, coef_danger, weight, tax)

    def save_to_database(self, year, object_name, class_danger, coef_danger, weight, tax):
        cursor = db.cursor()

        # Replace the table and column names with your actual database structure
        query = """
            INSERT INTO taxes_placement (year, objectName, classDanger, coefDanger, weight, tax)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (year, object_name, class_danger, coef_danger, weight, tax)

        cursor.execute(query, values)
        db.commit()

        cursor.close()

    def view_records(self):
        # Clear existing items in the Treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        cursor = db.cursor()

        # Replace the table and column names with your actual database structure
        query = """
            SELECT year, objectName, classDanger, coefDanger, weight, tax
            FROM taxes_placement
        """
        cursor.execute(query)

        records = cursor.fetchall()

        for record in records:
            self.treeview.insert("", "end", values=record)

        cursor.close()

    def setup_treeview(self):
        columns = ("Year", "Object Name", "Danger Class", "Waste Zone", "Weight (tons)", "Tax")
        self.treeview = ttk.Treeview(self.records_tab, columns=columns, show="headings")

        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=100)  # Adjust width as needed

        self.treeview.pack()

if __name__ == "__main__":
    root = Tk()
    app = WasteTaxCalculator(root)
    root.mainloop()

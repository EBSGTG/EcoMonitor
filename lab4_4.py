import mysql.connector
from tkinter import *
from tkinter import ttk
from enum import Enum

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1809",
    database="ecomon"
)

class ObjectName(Enum):
    PTAHOKOMPLEX_GUBIN = 'ТзОВ «Птахокомплекс Губин»'
    LOKACHYNSKIY_CVNTK = 'Локачинський ЦВНТК ПАТ «Укргазвидобування»'
    VOLYNTORF = 'ДП «Волиньторф»'
    FREE = 'FREE'

class WasteCategory(Enum):
    HIGHLY_ACTIVE = 'Високоактивні'
    MEDIUM_LOW_ACTIVE = 'Середньоактивні та низькоактивні'

class RadiationTaxCalculator:
    def __init__(self, root):
        self.root = root
        root.title("Radiation Waste Tax Calculator")

        Label(root, text="Year:").pack()
        self.year_entry = Entry(root)
        self.year_entry.pack()

        Label(root, text="Object Name:").pack()
        self.object_var = ttk.Combobox(root, values=[obj.value for obj in ObjectName])
        self.object_var.set('')
        self.object_var.pack()

        Label(root, text="Waste Category:").pack()
        self.category_var = StringVar(root)
        self.category_var.set(WasteCategory.HIGHLY_ACTIVE.value)
        category_menu = OptionMenu(root, self.category_var, *list(map(lambda x: x.value, WasteCategory)))
        category_menu.pack()

        Label(root, text="Quantity of Stored Waste:").pack()
        self.quantity_entry = Entry(root)
        self.quantity_entry.pack()

        self.calculate_button = Button(root, text="Calculate Tax", command=self.calculate_tax)
        self.calculate_button.pack()

        self.result_label = Label(root, text="")
        self.result_label.pack()

        self.view_records_button = Button(root, text="View Records", command=self.view_records)
        self.view_records_button.pack()

        # Add Treeview for displaying records
        self.setup_treeview()

    def calculate_tax(self):
        year = int(self.year_entry.get())
        object_name = self.object_var.get()
        waste_category = WasteCategory(self.category_var.get())
        stored_waste_quantity = float(self.quantity_entry.get())

        # Fixed value for electricity produced
        electricity_produced = 10000

        # Calculate tax based on the given conditions
        base_tax_rate = 0.0133
        tax = base_tax_rate * electricity_produced

        # Apply correction factor based on waste category
        correction_factor = 50 if waste_category == WasteCategory.HIGHLY_ACTIVE else 2
        tax *= correction_factor

        # Display the calculated tax
        self.result_label.config(text=f"Calculated Tax: {tax}")

        # Save the data to the database
        self.save_to_database(year, object_name, waste_category.value, stored_waste_quantity, tax)

    def save_to_database(self, year, object_name, category_danger, value_electricity, tax):
        cursor = db.cursor()

        # Replace the table and column names with your actual database structure
        query = """
            INSERT INTO taxes_radiation (year, objectName, CategoryDanger, valueElectricity, tax)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (year, object_name, category_danger, value_electricity, tax)

        cursor.execute(query, values)
        db.commit()

        cursor.close()

    def view_records(self):
        # Open a new window for displaying records
        records_window = Toplevel(self.root)
        records_window.title("Records")

        # Add Treeview for displaying records
        self.setup_treeview(records_window)

        # Fetch and display records
        self.fetch_and_display_records()

    def fetch_and_display_records(self):
        # Clear existing items in the Treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        cursor = db.cursor()

        # Replace the table and column names with your actual database structure
        query = """
            SELECT year, objectName, CategoryDanger, valueElectricity, tax
            FROM taxes_radiation
        """
        cursor.execute(query)

        records = cursor.fetchall()

        for record in records:
            self.treeview.insert("", "end", values=record)

        cursor.close()

    def setup_treeview(self, window=None):
        if window:
            # Treeview for displaying records in the given window
            treeview = ttk.Treeview(window, columns=("Year", "Object Name", "Waste Category", "Electricity Produced", "Tax"), show="headings")
            treeview.pack()

            columns = ("Year", "Object Name", "Waste Category", "Electricity Produced", "Tax")
            for col in columns:
                treeview.heading(col, text=col)
                treeview.column(col, width=100)  # Adjust width as needed

            # Save the treeview for future use
            self.treeview = treeview

if __name__ == "__main__":
    root = Tk()
    app = RadiationTaxCalculator(root)
    root.mainloop()

import mysql.connector
from tkinter import *
from tkinter import ttk
from enum import Enum

class WasteCategory(Enum):
    HIGHLY_ACTIVE = 'Високоактивні'
    MEDIUM_LOW_ACTIVE = 'Середньоактивні та низькоактивні'

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

class RadiationTaxCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Radiation Waste Tax Calculator")

        Label(root, text="Year:").pack()
        self.year_entry = Entry(root)
        self.year_entry.pack()

        self.object_label = Label(root, text="Object Name:")
        self.object_label.pack()

        self.object_var = StringVar()
        self.object_dropdown = OptionMenu(root, self.object_var, *[obj.value for obj in ObjectName])
        self.object_dropdown.pack()

        Label(root, text="Waste Category:").pack()
        self.category_var = StringVar(root)
        self.category_var.set(WasteCategory.HIGHLY_ACTIVE.value)
        category_menu = OptionMenu(root, self.category_var, *list(map(lambda x: x.value, WasteCategory)))
        category_menu.pack()

        Label(root, text="Volume (cubic meters):").pack()
        self.volume_entry = Entry(root)
        self.volume_entry.pack()

        Label(root, text="Storage Time (years):").pack()
        self.time_entry = Entry(root)
        self.time_entry.pack()

        Label(root, text="Contains Ionizing Radiation Sources:").pack()
        self.radiation_var = BooleanVar(root)
        self.radiation_checkbox = Checkbutton(root, variable=self.radiation_var)
        self.radiation_checkbox.pack()

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
        volume = float(self.volume_entry.get())
        time = float(self.time_entry.get())
        contains_radiation = self.radiation_var.get()

        # Perform tax calculation based on the given conditions
        if waste_category == WasteCategory.HIGHLY_ACTIVE:
            if contains_radiation:
                tax = 21084.66 * volume * time
            else:
                tax = 632539.66 * volume * time
        else:  # MEDIUM_LOW_ACTIVE
            if contains_radiation:
                tax = 4216.92 * volume * time
            else:
                tax = 11807.40 * volume * time

        # Display the calculated tax
        self.result_label.config(text=f"Calculated Tax: {tax}")

        # Save the data to the database
        self.save_to_database(year, object_name, waste_category, contains_radiation, volume, time, tax)

    def save_to_database(self, year, object_name, category_danger, contains_radiation, value_volume, time, tax):
        cursor = db.cursor()

        # Replace the table and column names with your actual database structure
        query = """
            INSERT INTO taxes_temporaryRadiation (year, objectName, CategoryDanger, valueVolume, time, tax)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (year, object_name, category_danger.value, value_volume, time, tax)

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
            SELECT year, objectName, CategoryDanger, valueVolume, time, tax
            FROM taxes_temporaryRadiation
        """
        cursor.execute(query)

        records = cursor.fetchall()

        for record in records:
            self.treeview.insert("", "end", values=record)

        cursor.close()

    def setup_treeview(self, window=None):
        if window:
            # Treeview for displaying records in the given window
            treeview = ttk.Treeview(window, columns=("Year", "Object Name", "Waste Category",  "Volume", "Time", "Tax"), show="headings")
            treeview.pack()

            columns = ("Year", "Object Name", "Waste Category",  "Volume", "Time", "Tax")
            for col in columns:
                treeview.heading(col, text=col)
                treeview.column(col, width=100)  # Adjust width as needed

            # Save the treeview for future use
            self.treeview = treeview


if __name__ == "__main__":
    root = Tk()
    app = RadiationTaxCalculator(root)
    root.mainloop()

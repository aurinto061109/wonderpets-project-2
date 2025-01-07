import tkinter as tk
from tkinter import messagebox, ttk
import csv

class InventoryModel:
    def __init__(self):
        self.inventory_data = []
        self.initialize_inventory()

    def initialize_inventory(self):
        initial_items = [
            ("BP001", "Ballpen", "100", "0", "0"),  # Ballpen
            ("P002", "Paper", "200", "0", "0"),     # Paper
            ("N003", "Notebook", "150", "0", "0"),  # Notebook
            ("B004", "Book", "300", "0", "0"),      # Book
            ("BG005", "Bag", "250", "0", "0"),      # Bag
            ("T006", "Tub", "180", "0", "0"),       # Tub
            ("E007", "Extender", "220", "0", "0"),  # Extender
            ("C008", "Charger", "160", "0", "0"),   # Charger
            ("H009", "Headphones", "140", "0", "0"),# Headphones
            ("PH010", "Phone", "200", "0", "0"),    # Phone
        ]
        for code, name, starting, received, shipped in initial_items:
            self.add_item(code, name, starting, received, shipped)

    def add_item(self, code, name, starting, received, shipped):
        try:
            starting = int(starting)
            received = int(received)
            shipped = int(shipped)

            if starting < 0 or received < 0 or shipped < 0:
                raise ValueError("Starting inventory, received, and shipped quantities must be non-negative.")

            on_hand = starting + received - shipped

            if on_hand < 0:
                raise ValueError(
                    f"Invalid inventory data: The on-hand inventory cannot be negative. "
                    f"Starting: {starting}, Received: {received}, Shipped: {shipped}"
                )

            self.inventory_data.append((code, name, starting, received, shipped, on_hand))

        except ValueError as e:
            raise ValueError(f"Error adding item: {e}")


    def search_item(self, search_term):
        return [item for item in self.inventory_data if item[0] == search_term or item[1].lower() == search_term.lower()]

    def edit_item(self, index, code, name, starting, received, shipped):
        on_hand = int(starting) + int(received) - int(shipped)
        self.inventory_data[index] = (code, name, starting, received, shipped, on_hand)

    def delete_item(self, index):
        del self.inventory_data[index]

    def export_data(self, filename):
        with open(filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Product Code", "Product Name", "Starting Inventory", "Received", "Shipped", "On Hand"])
            writer.writerows(self.inventory_data)

class InventoryView:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.root.title("Inventory Management System - Wonderpets")
        self.root.geometry("1080x500")

        self.create_inventory_table()
        self.create_form_inputs()
        self.create_buttons()

    def create_inventory_table(self):
        self.table_frame = tk.LabelFrame(self.root, text="Inventory", bg="lightgray", fg="black",font=("Times New Roman", 14))
        self.table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(self.table_frame, columns=("Code", "Name", "Starting Inventory", "Received", "Shipped", "On Hand"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def create_form_inputs(self):
        self.form_frame = tk.LabelFrame(self.root, text="Manage Inventory", bg="lightgray")
        self.form_frame.pack(fill="x", padx=20, pady=10)

        self.code_entry = self.create_label_entry(self.form_frame, "Product Code:", 0)
        self.starting_entry = self.create_label_entry(self.form_frame, "Starting Inventory:", 1)
        self.received_entry = self.create_label_entry(self.form_frame, "Received:", 2)
        self.shipped_entry = self.create_label_entry(self.form_frame, "Shipped:", 3)

    def create_label_entry(self, parent, label_text, row):
        ttk.Label(parent, text=label_text).grid(row=row, column=0, padx=5, pady=5)
        entry = ttk.Entry(parent)
        entry.grid(row=row, column=1, padx=5, pady=5)
        return entry

    def create_buttons(self):
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill="x", padx=20, pady=10)

        self.add_button = ttk.Button(self.button_frame, text="Add")
        self.add_button.grid(row=0, column=0, padx=10)

        self.edit_button = ttk.Button(self.button_frame, text="Edit")
        self.edit_button.grid(row=0, column=1, padx=10)

        self.delete_button = ttk.Button(self.button_frame, text="Delete")
        self.delete_button.grid(row=0, column=2, padx=10)

        self.export_button = ttk.Button(self.button_frame, text="Export")
        self.export_button.grid(row=0, column=3, padx=10)

        self.search_button = ttk.Button(self.button_frame, text="Search", command=self.open_search_window)
        self.search_button.grid(row=0, column=4, padx=10)

        self.show_all_button = ttk.Button(self.button_frame, text="Show All")
        self.show_all_button.grid(row=0, column=5, padx=10)


    def get_form_data(self):
        return (
            self.code_entry.get(),
            self.starting_entry.get(),
            self.received_entry.get(),
            self.shipped_entry.get()
        )

    def clear_form(self):
        self.code_entry.delete(0, tk.END)
        self.starting_entry.delete(0, tk.END)
        self.received_entry.delete(0, tk.END)
        self.shipped_entry.delete(0, tk.END)

    def update_inventory_table(self, inventory_data):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in inventory_data:
            self.tree.insert("", "end", values=row)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def show_warning(self, title, message):
        messagebox.showwarning(title, message)

    def show_all_items(self, inventory_data):
        self.update_inventory_table(inventory_data)

    def open_add_item_popup(self, callback):
        popup = tk.Toplevel(self.root)
        popup.title("Add New Item")
        popup.geometry("300x400")

        ttk.Label(popup, text="Product Code:").pack(pady=5)
        code_entry = ttk.Entry(popup)
        code_entry.pack(pady=5)

        ttk.Label(popup, text="Product Name:").pack(pady=5)
        name_entry = ttk.Entry(popup)
        name_entry.pack(pady=5)

        ttk.Label(popup, text="Starting Inventory:").pack(pady=5)
        starting_entry = ttk.Entry(popup)
        starting_entry.pack(pady=5)

        ttk.Label(popup, text="Received:").pack(pady=5)
        received_entry = ttk.Entry(popup)
        received_entry.pack(pady=5)

        ttk.Label(popup, text="Shipped:").pack(pady=5)
        shipped_entry = ttk.Entry(popup)
        shipped_entry.pack(pady=5)

        def submit():
            code = code_entry.get()
            name = name_entry.get()
            starting = starting_entry.get()
            received = received_entry.get()
            shipped = shipped_entry.get()
            callback(code, name, starting, received, shipped)
            popup.destroy()

        ttk.Button(popup, text="Add Item", command=submit).pack(pady=20)

    def open_edit_item_popup(self, code, name, starting, received, shipped, callback):
        popup = tk.Toplevel(self.root)
        popup.title("Edit Item")
        popup.geometry("300x400")

        ttk.Label(popup, text="Product Code:").pack(pady=5)
        code_entry = ttk.Entry(popup)
        code_entry.insert(0, code)
        code_entry.pack(pady=5)

        ttk.Label(popup, text="Product Name:").pack(pady=5)
        name_entry = ttk.Entry(popup)
        name_entry.insert(0, name)
        name_entry.pack(pady=5)

        ttk.Label(popup, text="Starting Inventory:").pack(pady=5)
        starting_entry = ttk.Entry(popup)
        starting_entry.insert(0, starting)
        starting_entry.pack(pady=5)

        ttk.Label(popup, text="Received:").pack(pady= 5)
        received_entry = ttk.Entry(popup)
        received_entry.insert(0, received)
        received_entry.pack(pady=5)

        ttk.Label(popup, text="Shipped:").pack(pady=5)
        shipped_entry = ttk.Entry(popup)
        shipped_entry.insert(0, shipped)
        shipped_entry.pack(pady=5)

        def submit():
            code = code_entry.get()
            name = name_entry.get()
            starting = starting_entry.get()
            received = received_entry.get()
            shipped = shipped_entry.get()
            callback(code, name, starting, received, shipped)
            popup.destroy()

        ttk.Button(popup, text="Update Item", command=submit).pack(pady=20)

    def open_search_window(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Inventory")
        search_window.geometry("300x200")

        ttk.Label(search_window, text="Enter Product Code or Name:").pack(pady=10)
        search_entry = ttk.Entry(search_window)
        search_entry.pack(pady=5)

        def perform_search():
            search_term = search_entry.get()
            results = self.model.search_item(search_term)
            if results:
                self.update_inventory_table(results)
            else:
                self.show_warning("Search Error", "No item found with that code or name.")

        search_button = ttk.Button(search_window, text="Search", command=perform_search)
        search_button.pack(pady=20)

class InventoryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.add_button.config(command=self.open_add_item_popup)
        self.view.edit_button.config(command=self.open_edit_item_popup)
        self.view.delete_button.config(command=self.delete_inventory)
        self.view.export_button.config(command=self.export_inventory)
        self.view.show_all_button.config(command=self.show_all_inventory)

    def open_add_item_popup(self):
        self.view.open_add_item_popup(self.add_inventory)

    def open_edit_item_popup(self):
        selected_item = self.view.tree.selection()
        if not selected_item:
            self.view.show_warning("Selection Error", "Please select an item to edit.")
            return

        index = self.view.tree.index(selected_item[0])
        item = self.model.inventory_data[index]
        self.view.open_edit_item_popup(item[0], item[1], item[2], item[3], item[4], self.update_inventory)

    def add_inventory(self, code, name, starting, received, shipped):
        if code and name and starting.isdigit() and received.isdigit() and shipped.isdigit():
            existing_item = self.model.search_item(code)
            if not existing_item:  # Only add if the item does not exist
                self.model.add_item(code, name, starting, received, shipped)
                self.view.update_inventory_table(self.model.inventory_data)
            else:
                self.view.show_warning("Input Error", "Product code already exists.")
        else:
            self.view.show_warning("Input Error", "Please provide valid inputs.")

    def update_inventory(self, code, name, starting, received, shipped):
        selected_item = self.view.tree.selection()
        if not selected_item:
            self.view.show_warning("Selection Error", "Please select an item to update.")
            return

        index = self.view.tree.index(selected_item[0])
        if code and name and starting.isdigit() and received.isdigit() and shipped.isdigit():
            self.model.edit_item(index, code, name, starting, received, shipped)
            self.view.update_inventory_table(self.model.inventory_data)
            self.view.clear_form()
        else:
            self.view.show_warning("Input Error", "Please provide valid inputs.")

    def delete_inventory(self):
        selected_item = self.view.tree.selection()
        if not selected_item:
            self.view.show_warning("Selection Error", "Please select an item to delete.")
            return

        index = self.view.tree.index(selected_item[0])
        self.model.delete_item(index)
        self.view.update_inventory_table(self.model.inventory_data)

    def export_inventory(self):
        if not self.model.inventory_data:
            self.view.show_warning("Export Error", "No data to export.")
            return

        self.model.export_data("Inventory_Data.csv")
        self.view.show_message("Export Success", "Data exported to Inventory_Data.csv.")

    def show_all_inventory(self):
        self.view.show_all_items(self.model.inventory_data)
    

if __name__ == "__main__":
    root = tk.Tk()
    model = InventoryModel()
    view = InventoryView(root, model)
    controller = InventoryController(model, view)
    root.mainloop()
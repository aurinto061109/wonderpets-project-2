import tkinter as tk
from tkinter import messagebox, ttk
import csv

class InventoryModel:
    def __init__(self):
        self.inventory_data = []

    def add_item(self, code, starting, received, shipped):
        on_hand = int(starting) + int(received) - int(shipped)
        self.inventory_data.append((code, starting, received, shipped, on_hand))

    def edit_item(self, index, code, starting, received, shipped):
        on_hand = int(starting) + int(received) - int(shipped)
        self.inventory_data[index] = (code, starting, received, shipped, on_hand)

    def delete_item(self, index):
        del self.inventory_data[index]

    def export_data(self, filename):
        with open(filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Product Code", "Starting Inventory", "Received", "Shipped", "On Hand"])
            writer.writerows(self.inventory_data)

class InventoryView:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System - wonderpets")
        self.root.geometry("700x500")

        self.create_inventory_table()
        self.create_form_inputs()
        self.create_buttons()

    def create_inventory_table(self):
        self.table_frame = ttk.LabelFrame(self.root, text="Inventory")
        self.table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(self.table_frame, columns=("Code", "Starting Inventory", "Received", "Shipped", "On Hand"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def create_form_inputs(self):
        self.form_frame = ttk.LabelFrame(self.root, text="Manage Inventory")
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
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(fill="x", padx=20, pady=10)

        self.add_button = ttk.Button(self.button_frame, text="Add")
        self.add_button.grid(row=0, column=0, padx=10)

        self.edit_button = ttk.Button(self.button_frame, text="Edit")
        self.edit_button.grid(row=0, column=1, padx=10)

        self.delete_button = ttk.Button(self.button_frame, text="Delete")
        self.delete_button.grid(row=0, column=2, padx=10)

        self.export_button = ttk.Button(self.button_frame, text="Export")
        self.export_button.grid(row=0, column=3, padx=10)

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

class InventoryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.add_button.config(command=self.add_inventory)
        self.view.edit_button.config(command=self.edit_inventory)
        self.view.delete_button.config(command=self.delete_inventory)
        self.view.export_button.config(command=self.export_inventory)

    def add_inventory(self):
        code, starting, received, shipped = self.view.get_form_data()
        if code and starting.isdigit() and received.isdigit() and shipped.isdigit():
            self.model.add_item(code, starting, received, shipped)
            self.view.update_inventory_table(self.model.inventory_data)
            self.view.clear_form()
        else:
            self.view.show_warning("Input Error", "Please provide valid inputs.")

    def edit_inventory(self):
        selected_item = self.view.tree.selection()
        if not selected_item:
            self.view.show_warning("Selection Error", "Please select an item to edit.")
            return

        index = self.view.tree.index(selected_item[0])
        code, starting, received, shipped = self.view.get_form_data()
        if code and starting.isdigit() and received.isdigit() and shipped.isdigit():
            self.model.edit_item(index, code, starting, received, shipped)
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

if __name__ == "__main__":
    root = tk.Tk()
    model = InventoryModel()
    view = InventoryView(root)
    controller = InventoryController(model, view)
    root.mainloop()

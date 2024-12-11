import tkinter as tk
from tkinter import messagebox, ttk
import csv

class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System - wonderpets")
        self.root.geometry("700x500")  
        self.inventory_data = []

        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 10), foreground="#333333")
        style.configure("TButton", font=("Helvetica", 10), foreground="white")
        style.configure("TFrame", background="#F5F5F5")
        style.configure("Treeview", font=("Helvetica", 10))
        style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))

        self.create_inventory_table()
        self.create_form_inputs()
        self.create_buttons()

    def create_inventory_table(self):
        self.table_frame = ttk.LabelFrame(self.root, text="Inventory")
        self.table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree = ttk.Treeview(self.table_frame, columns=("Code", "Starting Inventory", "Received", "Shipped", "On Hand"), show="headings")
        self.tree.heading("Code", text="Product Code")
        self.tree.heading("Starting Inventory", text="Starting Inventory")
        self.tree.heading("Received", text="Inventory Received")
        self.tree.heading("Shipped", text="Inventory Shipped")
        self.tree.heading("On Hand", text="Inventory on Hand")

        self.tree.column("Code", width=150, anchor="center")
        self.tree.column("Starting Inventory", width=150, anchor="center")
        self.tree.column("Received", width=150, anchor="center")
        self.tree.column("Shipped", width=150, anchor="center")
        self.tree.column("On Hand", width=150, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def create_form_inputs(self):
        self.form_frame = ttk.LabelFrame(self.root, text="Manage Inventory")
        self.form_frame.pack(fill="x", padx=20, pady=10)

        ttk.Label(self.form_frame, text="Product Code:").grid(row=0, column=0, padx=5, pady=5)
        self.code_entry = ttk.Entry(self.form_frame)
        self.code_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Starting Inventory:").grid(row=0, column=2, padx=5, pady=5)
        self.starting_entry = ttk.Entry(self.form_frame)
        self.starting_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Received:").grid(row=1, column=0, padx=5, pady=5)
        self.received_entry = ttk.Entry(self.form_frame)
        self.received_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Shipped:").grid(row=1, column=2, padx=5, pady=5)
        self.shipped_entry = ttk.Entry(self.form_frame)
        self.shipped_entry.grid(row=1, column=3, padx=5, pady=5)

    def create_buttons(self):
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(fill="x", padx=20, pady=10)

        add_button = ttk.Button(self.button_frame, text="Add", command=self.add_inventory)
        add_button.grid(row=0, column=0, padx=10)
        add_button.configure(style="Green.TButton")

        edit_button = ttk.Button(self.button_frame, text="Edit", command=self.edit_inventory)
        edit_button.grid(row=0, column=1, padx=10)
        edit_button.configure(style="Green.TButton")

        delete_button = ttk.Button(self.button_frame, text="Delete", command=self.delete_inventory)
        delete_button.grid(row=0, column=2, padx=10)
        delete_button.configure(style="Green.TButton")

        export_button = ttk.Button(self.button_frame, text="Export", command=self.export_inventory)
        export_button.grid(row=0, column=3, padx=10)
        export_button.configure(style="Green.TButton")

        style = ttk.Style()
        style.configure("Green.TButton", background="#4CAF50", foreground="white")

    def add_inventory(self):
        code = self.code_entry.get()
        starting = self.starting_entry.get()
        received = self.received_entry.get()
        shipped = self.shipped_entry.get()

        if code and starting.isdigit() and received.isdigit() and shipped.isdigit():
            on_hand = int(starting) + int(received) - int(shipped)
            self.tree.insert("", "end", values=(code, starting, received, shipped, on_hand))
            self.clear_form()
        else:
            messagebox.showwarning("Input Error", "Please provide valid inputs.")

    def edit_inventory(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select an item to edit.")
            return

        code = self.code_entry.get()
        starting = self.starting_entry.get()
        received = self.received_entry.get()
        shipped = self.shipped_entry.get()

        if code and starting.isdigit() and received.isdigit() and shipped.isdigit():
            on_hand = int(starting) + int(received) - int(shipped)
            self.tree.item(selected_item, values=(code, starting, received, shipped, on_hand))
            self.clear_form()
        else:
            messagebox.showwarning("Input Error", "Please provide valid inputs.")

    def delete_inventory(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select an item to delete.")
            return

        self.tree.delete(selected_item)

    def export_inventory(self):
        if not self.tree.get_children():
            messagebox.showwarning("Export Error", "No data to export.")
            return

        with open("Inventory_Data.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Product Code", "Starting Inventory", "Received", "Shipped", "On Hand"])

            for row_id in self.tree.get_children():
                row = self.tree.item(row_id, "values")
                writer.writerow(row)

        messagebox.showinfo("Export Success", "Data exported to Inventory_Data.csv.")

    def clear_form(self):
        self.code_entry.delete(0, tk.END)
        self.starting_entry.delete(0, tk.END)
        self.received_entry.delete(0, tk.END)
        self.shipped_entry.delete(0, tk.END)
        self.code_entry.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagementApp(root)
    root.mainloop()

    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 10), foreground="#333333")
    style.configure("TButton", font=("Helvetica", 10), foreground="white")
    style.configure("TFrame", background="#F5F5F5")
    style.configure("Treeview", font=("Helvetica", 10))
    style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))

    self.create_inventory_table()
    self.create_form_inputs()
    self.create_buttons()

def create_inventory_table(self):
    self.table_frame = ttk.LabelFrame(self.root, text="Inventory")
    self.table_frame.pack(fill="both", expand=True, padx=20, pady=10)

    self.tree = ttk.Treeview(self.table_frame, columns=("Code", "Starting Inventory", "Received", "Shipped", "On Hand"), show="headings")
    self.tree.heading("Code", text="Product Code")
    self.tree.heading("Starting Inventory", text="Starting Inventory")
    self.tree.heading("Received", text="Inventory Received")
    self.tree.heading("Shipped", text="Inventory Shipped")
    self.tree.heading("On Hand", text="Inventory on Hand")

    self.tree.column("Code", width=150, anchor="center")
    self.tree.column("Starting Inventory", width=150, anchor="center")
    self.tree.column("Received", width=150, anchor="center")
    self.tree.column("Shipped", width=150, anchor="center")
    self.tree.column("On Hand", width=150, anchor="center")

    self.tree.pack(fill="both", expand=True, padx=10, pady=10)

def create_form_inputs(self):
    self.form_frame = ttk.LabelFrame(self.root, text="Manage Inventory")
    self.form_frame.pack(fill="x", padx=20, pady=10)

    ttk.Label(self.form_frame, text="Product Code:").grid(row=0, column=0, padx=5, pady=5)
    self.code_entry = ttk.Entry(self.form_frame)
    self.code_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(self.form_frame, text="Starting Inventory:").grid(row=0, column=2, padx=5, pady=5)
    self.starting_entry = ttk.Entry(self.form_frame)
    self.starting_entry.grid(row=0, column=3, padx=5, pady=5)

    ttk.Label(self.form_frame, text="Received:").grid(row=1, column=0, padx=5, pady=5)
    self.received_entry = ttk.Entry(self.form_frame)
    self.received_entry.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(self.form_frame, text="Shipped:").grid(row=1, column=2, padx=5, pady=5)
    self.shipped_entry = ttk.Entry(self.form_frame)
    self.shipped_entry.grid(row=1, column=3, padx=5, pady=5)

def create_buttons(self):
    self.button_frame = ttk.Frame(self.root)
    self.button_frame.pack(fill="x", padx=20, pady=10)

    add_button = ttk.Button(self.button_frame, text="Add", command=self.add_inventory)
    add_button.grid(row=0, column=0, padx=10)
    add_button.configure(style="Green.TButton")

    edit_button = ttk.Button(self.button_frame, text="Edit", command=self.edit_inventory)
    edit_button.grid(row=0, column=1, padx=10)
    edit_button.configure(style="Green.TButton")

    delete_button = ttk.Button(self.button_frame, text="Delete", command=self.delete_inventory)
    delete_button.grid(row=0, column=2, padx=10)
    delete_button.configure(style="Green.TButton")

    export_button = ttk.Button(self.button_frame, text="Export", command=self.export_inventory)
    export_button.grid(row=0, column=3, padx=10)
    export_button.configure(style="Green.TButton")

    style = ttk.Style()
    style.configure("Green.TButton", background="#4CAF50", foreground="white")

def add_inventory(self):
    code = self.code_entry.get()
    starting = self.starting_entry.get()
    received = self.received_entry.get()
    shipped = self.shipped_entry.get()

    if code and starting.isdigit() and received.isdigit() and shipped.isdigit():
        on_hand = int(starting) + int(received) - int(shipped)
        self.tree.insert("", "end", values=(code, starting, received, shipped, on_hand))
        self.clear_form()
    else:
        messagebox.showwarning("Input Error", "Please provide valid inputs.")

def edit_inventory(self):
    selected_item = self.tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to edit.")
        return

    code = self.code_entry.get()
    starting = self.starting_entry.get()
    received = self.received_entry.get()
    shipped = self.shipped_entry.get()

    if code and starting.isdigit() and received.isdigit() and shipped.isdigit():
        on_hand = int(starting) + int(received) - int(shipped)
        self.tree.item(selected_item, values=(code, starting, received, shipped, on_hand))
        self.clear_form()
    else:
        messagebox.showwarning("Input Error", "Please provide valid inputs.")

def delete_inventory(self):
    selected_item = self.tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to delete.")
        return

    self.tree.delete(selected_item)

def export_inventory(self):
    if not self.tree.get_children():
        messagebox.showwarning("Export Error", "No data to export.")
        return

    with open("Inventory_Data.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product Code", "Starting Inventory", "Received", "Shipped", "On Hand"])

        for row_id in self.tree.get_children():
            row = self.tree.item(row_id, "values")
            writer.writerow(row)

    messagebox.showinfo("Export Success", "Data exported to Inventory_Data.csv.")

def clear_form(self):
    self.code_entry.delete(0, tk.END)
    self.starting_entry.delete(0, tk.END)
    self.received_entry.delete(0, tk.END)
    self.shipped_entry.delete(0, tk.END)
    self.code_entry.focus_set()
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import simpledialog
import csv

class POSModel:
    def __init__(self):
        self.cart = []
        self.inventory = [
    ("BP001", "Ballpen", 100),
    ("P002", "Paper", 200),
    ("N003", "Notebook", 150),
    ("B004", "Book", 300),
    ("BG005", "Bag", 250),
    ("T006", "Tub", 180),
    ("P007", "Pencil", 120),
    ("E008", "Eraser", 50),
    ("R009", "Ruler", 75),
    ("S010", "Scissors", 90),
    ("C011", "Calculator", 400),
    ("F012", "Folder", 60),
    ("S013", "Stapler", 150),
    ("S014", "Sticky Notes", 80),
    ("H015", "Highlighter", 110),
    ("M016", "Marker", 95),
    ("C017", "Crayons", 130),
    ("P018", "Paint Set", 220),
    ("B019", "Binder", 140),
    ("T020", "Tape", 70),
    ("C021", "Chalk", 30),
    ("W022", "Whiteboard Marker", 85),
    ("D023", "Drawing Pad", 160),
    ("P024", "Pencil Case", 100),
    ("G025", "Glue", 55),
    ("P026", "Poster Board", 120),
    ("S027", "Sketchbook", 180),
    ("C028", "Colored Pencils", 150),
    ("F029", "Flashcards", 90),
    ("B030", "Book Cover", 40),
    ("P031", "Protractor", 65),
    ("T032", "Tack Board", 200),
    ("C033", "Compass", 75),
    ("N034", "Notebook Divider", 50),
    ("S035", "Sticky Tabs", 45),
    ("P036", "Pencil Sharpener", 30),
    ("R037", "Report Cover", 55),
    ("B038", "Bulletin Board", 250),
    ("C039", "Calculator Battery", 20),
    ("D040", "Desk Organizer", 150),
    ("P041", "Paintbrush", 60),
    ("S042", "Science Kit", 300),
    ("H043", "Homework Planner", 80),
    ("B044", "Bookmark", 25),
    ("C045", "Clipboard", 70),
    ("F046", "Fountain Pen", 200),
    ("M047", "Math Set", 120),
    ("S048", "Student Planner", 90),
    ("T049", "Textbook", 350),
    ("W050", "Watercolor Set", 220),
    ("C051", "Construction Paper", 100),
    ("P052", "Pencil Grip", 15),
    ("E053", "Envelope", 40),
    ("R054", "Rubber Bands", 30),
    ("S055", "Sponge", 25),
    ("T056", "Tissue Paper", 50),
    ("C057", "Colored Markers", 130),
    ("B058", "Bristol Board", 90),
    ("D059", "Drawing Compass", 40),
    ("P060", "Plastic Folder", 60),
    ("S061", "Science Project Board", 150),
    ("C062", "Craft Scissors", 80),
    ("P063", "Pencil Set", 110),
    ("B064", "Book Stand", 100),
    ("F065", "File Organizer", 120),
    ("N066", "Notebook with Pockets", 160),
    ("S067", "Study Guide", 70),
    ("C068", "Calculator Case", 30),
    ("P069", "Paint Palette", 50),
    ("R070", "Reading Log", 40),
    ("S071", "Sculpting Clay", 90),
    ("T072", "Tote Bag", 150),
    ("C073", "Craft Paper", 80),
    ("B074", "Binder Clips", 25),
    ("P075", "Pencil Box", 100),
    ("S076", "Science Lab Kit", 300),
    ("H077", "Homework Folder", 60),
    ("C078", "Chalkboard", 200),
    ("P079", "Poster Markers", 70),
    ("S080", "Study Flashcards", 90),
    ("B081", "Bookmarks Set", 30),
    ("C082", "Colored Chalk", 40),
    ("P083", "Pencil Ruler", 50),
    ("S084", "Sketch Pencils", 120),
    ("B085", "Bookmarks", 25),
    ("C086", "Craft Glue", 45),
    ("F087", "Folding Ruler", 60),
    ("N088", "Notebook with Grid", 150),
    ("S089", "Science Experiment Kit", 250),
    ("T090", "Transparent Folder", 70),
    ("C091", "Coloring Book", 80),
    ("P092", "Paint Marker", 90),
    ("R093", "Rubber Eraser", 20),
    ("S094", "Sewing Kit", 100),
    ("B095", "Bookbinding Kit", 200),
    ("C096", "Crafting Tools", 150),
    ("P097", "Pencil Stencils", 40),
    ("S098", "Study Planner", 60),
    ("T099", "Tack Pins", 30),
    ("C100", "Calligraphy Set", 120),
    ("P101", "Plastic Ruler", 25),
    ("S102", "Science Textbook", 300),
    ("B103", "Binder with Zipper", 150),
    ("C104", "Colored Paper", 70),
    ("P105", "Pencil Case with Compartments", 80),
    ("S106", "Sketching Paper", 90),
    ("B107", "Bookbinding Tape", 40),
    ("C108", "Crafting Paper", 60),
    ("P109", "Pencil with Grip", 30),
    ("S110", "Student ID Holder", 20),
    ("B111", "Booklight", 100),
    ("C112", "Chalk Holder", 15),
    ("P113", "Paintbrush Set", 70),
    ("S114", "Science Fair Display Board", 200),
    ("B115", "Book Repair Kit", 150),
    ("C116", "Coloring Pencils Set", 130),
    ("P117", "Pencil Sharpener with Container", 50),
    ("S118", "Study Desk Organizer", 90),
    ("B119", "Book Cover Set", 40),
    ("C120", "Crafting Kit", 250),
    ("P121", "Pencil with Eraser", 20),
    ("S122", "Student Portfolio", 80),
    ("B123", "Bookends", 60),
    ("C124", "Chalkboard Eraser", 25),
    ("P125", "Paint Set with Brushes", 220),
    ("S126", "Science Lab Notebook", 150),
    ("B127", "Binder with Pockets", 100),
    ("C128", "Colored Sticky Notes", 45),
    ("P129", "Pencil with Lead Refills", 90),
    ("S130", "Study Guide Book", 70),
    ("B131", "Book Storage Box", 200),
    ("C132", "Crafting Scissors", 80),
    ("P133", "Pencil with Built-in Sharpener", 50),
    ("S134", "Student Study Kit", 300),
    ("B135", "Book Holder", 100),
    ("C136", "Chalkboard Paint", 150),
    ("P137", "Pencil with Color Lead", 40),
    ("S138", "Science Experiment Book", 90),
    ("B139", "Book Tote", 60),
    ("C140", "Colored Gel Pens", 130),
    ("P141", "Pencil with Grip and Eraser", 25),
    ("S142", "Student Resource Book", 80),
    ("B143", "Book Repair Tape", 20),
    ("C144", "Crafting Adhesive", 55),
    ("P145", "Pencil with Multi-Colors", 70),
    ("S146", "Study Skills Workbook", 150),
    ("B147", "Book Display Stand", 100),
    ("C148", "Chalkboard Stickers", 30),
    ("P149", "Pencil with Built-in Eraser", 20),
    ("S150", "Science Project Guide", 90),
    ("B151", "Book Journal", 40),
    ("C152", "Crafting Templates", 60),
    ("P153", "Pencil with Decorative Design", 50),
    ("S154", "Student Success Planner", 80),
    ("B155", "Book Storage Rack", 200),
    ("C156", "Colored Paper Clips", 25),
    ("P157", "Pencil with Refillable Lead", 100),
    ("S158", "Study Skills Guide", 70),
    ("B159", "Book Covering Film", 40),
    ("C160", "Crafting Stamps", 60),
    ("P161", "Pencil with Fun Patterns", 30),
    ("S162", "Science Fair Project Kit", 250),
    ("B163", "Book Bag with Compartments", 150),
    ("C164", "Chalkboard Markers", 80),
    ("P165", "Pencil with Colorful Designs", 50),
    ("S166", "Student Achievement Journal", 90),
    ("B167", "Book Protection Sleeve", 20),
    ("C168", "Crafting Beads", 55)
        ]
    
    def search_item(self, search_term):
        return [item for item in self.inventory if item[0] == search_term or item[1].lower() == search_term.lower()]
    
    def add_to_cart(self, item_code, quantity):
        item = next((item for item in self.inventory if item[0] == item_code), None)
        if item:
            self.cart.append((item[0], item[1], item[2], quantity, item[2] * quantity))
    
    def edit_cart_item(self, index, new_quantity):
        if 0 <= index < len(self.cart):
            item = self.cart[index]
            if new_quantity > 0:
                self.cart[index] = (item[0], item[1], item[2], new_quantity, item[2] * new_quantity)
            else:
                del self.cart[index]  # Remove item if quantity is 0
    
    def calculate_total(self):
        return sum(item[4] for item in self.cart)

    def export_cart_to_csv(self, filename="checkout.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Code", "Name", "Price", "Quantity", "Total Price"])
            for item in self.cart:
                writer.writerow(item)
        print(f"Cart exported to {filename}")

class POSView:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.root.title("NoteSchool Store")
        self.root.geometry("1080x800")
        self.root.configure(bg="#98FF98")

        self.style = ttk.Style()
        self.style.configure("Treeview", background="white", foreground="black", rowheight=25, font=("Courier New", 10))
        self.style.configure("Treeview.Heading", font=("Courier New", 12, "bold"))
        self.style.configure("TButton", font=("Courier New", 12, "bold"))

        self.create_widgets()

    def create_widgets(self):
        self.create_inventory_table()
        self.create_cart_table()
        self.create_buttons()

    def create_inventory_table(self):
        style = ttk.Style()
        style.configure("Custom.TLabelframe.Label", font=("Courier New", 13, "bold"))
        
        self.inventory_frame = ttk.LabelFrame(self.root, text="Available Products", style="Custom.TLabelframe")
        self.inventory_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree_inventory = ttk.Treeview(self.inventory_frame, columns=("Code", "Name", "Price"), show="headings")
        for col in self.tree_inventory["columns"]:
            self.tree_inventory.heading(col, text=col)
            self.tree_inventory.column(col, width=150, anchor="center")
        self.tree_inventory.pack(fill="both", expand=True, padx=10, pady=10)
        style.configure("Treeview", background="#ADD8E6", foreground="black", fieldbackground="#f0f0f0")

        self.update_inventory_table()

    def create_cart_table(self):
        style = ttk.Style()
        style.configure("Custom.TLabelframe.Label", font=("Courier New", 13, "bold"))

        self.cart_frame = ttk.LabelFrame(self.root, text="Cart", style="Custom.TLabelframe")
        self.cart_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tree_cart = ttk.Treeview(self.cart_frame, columns=("Code", "Name", "Price", "Quantity", "Total"), show="headings")
        for col in self.tree_cart["columns"]:
            self.tree_cart.heading(col, text=col)
            self.tree_cart.column(col, width=150, anchor="center")
        self.tree_cart.pack(fill="both", expand=True, padx=10, pady=10)

        self.total_label = ttk.Label(self.cart_frame, text="Total: ₱0.00", style="Custom.TLabelframe.Label")
        self.total_label.pack(pady=10)
        style.configure("Treeview", background="#ADD8E6", foreground="black", fieldbackground="#f0f0f0")

    def create_buttons(self):
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill="x", padx=20, pady=10)
        self.button_frame.configure(bg="#98FF98")

        self.add_button = ttk.Button(self.button_frame, text="Add to Cart", command=self.add_to_cart)
        self.add_button.grid(row=0, column=0, padx=10)

        self.edit_button = ttk.Button(self.button_frame, text="Edit", command=self.edit_cart_item)
        self.edit_button.grid(row=0, column=1, padx=10)

        self.remove_button = ttk.Button(self.button_frame, text="Remove", command=self.remove_cart_item)
        self.remove_button.grid(row=0, column=2, padx=10)

        self.search_button = ttk.Button(self.button_frame, text="Search", command=self.search_item)
        self.search_button.grid(row=0, column=3, padx=10)

        self.checkout_button = ttk.Button(self.button_frame, text="Checkout", command=self.checkout)
        self.checkout_button.grid(row=0, column=4, padx=10)

    def update_inventory_table(self):
        for item in self.tree_inventory.get_children():
            self.tree_inventory.delete(item)
        for row in self.model.inventory:
            self.tree_inventory.insert("", "end", values=row)

    def update_cart_table(self):
        for item in self.tree_cart.get_children():
            self.tree_cart.delete(item)
        for row in self.model.cart:
            self.tree_cart.insert("", "end", values=row)
        self.total_label.config(text=f"Total: ₱{self.model.calculate_total():.2f}")

    def show_warning(self, title, message):
        messagebox.showwarning(title, message)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def add_to_cart(self):
        selected_item = self.tree_inventory.selection()
        if not selected_item:
            self.show_warning("Selection Error", "Please select a product to add to the cart.")
            return

        item_code = self.tree_inventory.item(selected_item[0], "values")[0]
        quantity = simpledialog.askinteger("Quantity", "Enter quantity:", parent=self.root)
        if quantity and quantity > 0:
            self.model.add_to_cart(item_code, quantity)
            self.update_cart_table()
        else:
            self.show_warning("Invalid Quantity", "Please enter a valid quantity.")

    def edit_cart_item(self):
        selected_item = self.tree_cart.selection()
        if not selected_item:
            self.show_warning("Selection Error", "Please select an item in the cart to edit.")
            return

        index = self.tree_cart.index(selected_item[0])
        current_quantity = self.model.cart[index][3]
        new_quantity = simpledialog.askinteger("Edit Quantity", "Enter new quantity:", initialvalue=current_quantity, parent=self.root)
        if new_quantity is not None:
            self.model.edit_cart_item(index, new_quantity)
            self.update_cart_table()

    def remove_cart_item(self):
        selected_item = self.tree_cart.selection()
        if not selected_item:
            self.show_warning("Selection Error", "Please select an item in the cart to remove.")
            return

        index = self.tree_cart.index(selected_item[0])
        self.model.edit_cart_item(index, 0)  # Remove the item by setting quantity to 0
        self.update_cart_table()

    def search_item(self):
        search_term = simpledialog.askstring("Search", "Enter product code or name:", parent=self.root)
        if search_term:
            results = self.model.search_item(search_term)
            if results:
                self.show_message("Search Results", "\n".join([f"{item[0]}: {item[1]} - ${item[2]}" for item in results]))
            else:
                self.show_warning("No Results", "No products found matching your search.")

    def checkout(self):
        total = self.model.calculate_total()
        if total > 0:
            self.show_message("Checkout", f"Total amount: ₱{total:.2f}")
            self.model.export_cart_to_csv("checkout.csv")
            self.model.cart.clear()
            self.update_cart_table()
        else:
            self.show_warning("Empty Cart", "Your cart is empty.")

# Point of Sale Controller
class POSController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.view.update_inventory_table()

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    model = POSModel()
    view = POSView(root, model)
    controller = POSController(model, view)
    controller.run()
    root.mainloop()
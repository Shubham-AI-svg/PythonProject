# Importing necessary modules
import tkinter as tk
from tkinter import messagebox
import textile_management.products as tm_products

# Create the main application window
app = tk.Tk()
app.title("Textile Management System")

# Function to handle adding a new product to the list
def add_product_to_list():
    # Get user input from the GUI entry fields
    product_id = entry_id.get()
    product_name = entry_name.get()
    product_price = entry_price.get()
    product_quantity = entry_quantity.get()

    try:
        # Convert input to appropriate data types
        product_id = int(product_id)
        product_price = float(product_price)
        product_quantity = int(product_quantity)

        # Call the function to add the product to the list
        tm_products.add_product(product_id, product_name, product_price, product_quantity)

        # Show a success message to the user
        messagebox.showinfo("Success", "Product added successfully!")

        # Clear the input fields for the next entry
        clear_entries()

    except ValueError:
        # Show an error message for invalid input
        messagebox.showerror("Error", "Invalid input. Please enter valid details.")

# Function to display all products in the list
def view_products():
    # Clear the existing list
    products_list.delete(0, tk.END)

    # Get all products from the database
    all_products = tm_products.get_all_products()

    # Display each product in the list
    for product in all_products:
        products_list.insert(tk.END, str(product))

# Function to search for a product by ID
def search_product():
    # Get the product ID from the search entry field
    product_id = entry_search.get()

    try:
        # Convert the input to an integer
        product_id = int(product_id)

        # Get the product with the given ID
        product = tm_products.get_product_by_id(product_id)

        if product:
            # Clear the previous search result
            search_result_list.delete(0, tk.END)

            # Display the search result
            search_result_list.insert(tk.END, str(product))
        else:
            # If product not found, show a message
            messagebox.showinfo("Not Found", "Product not found.")

    except ValueError:
        # Show an error message for invalid product ID
        messagebox.showerror("Error", "Invalid product ID. Please enter a valid ID.")

# Function to clear all entry fields
def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("Textile Management System")
# Custom theme with linen background color
app.config(bg="#FAF0E6")  # Linen background color
app.geometry("600x400")  # Set window size
app.option_add("*Font", "Helvetica 10")  # Use Helvetica font with size 10

# Create GUI components
label_id = tk.Label(app, text="Product ID:")
label_name = tk.Label(app, text="Product Name:")
label_price = tk.Label(app, text="Price:")
label_quantity = tk.Label(app, text="Quantity:")
entry_id = tk.Entry(app)
entry_name = tk.Entry(app)
entry_price = tk.Entry(app)
entry_quantity = tk.Entry(app)

button_add = tk.Button(app, text="Add Product", command=add_product_to_list)
button_view = tk.Button(app, text="View All Products", command=view_products)
button_search = tk.Button(app, text="Search Product", command=search_product)
button_clear = tk.Button(app, text="Clear Entries", command=clear_entries)

products_list = tk.Listbox(app, width=50, height=10)

# Arrange GUI components using grid layout
label_id.grid(row=0, column=0)
label_name.grid(row=1, column=0)
label_price.grid(row=2, column=0)
label_quantity.grid(row=3, column=0)
entry_id.grid(row=0, column=1)
entry_name.grid(row=1, column=1)
entry_price.grid(row=2, column=1)
entry_quantity.grid(row=3, column=1)

button_add.grid(row=4, column=0, columnspan=2, pady=5)
button_view.grid(row=5, column=0, columnspan=2, pady=5)
button_search.grid(row=6, column=0, columnspan=2, pady=5)
button_clear.grid(row=7, column=0, columnspan=2, pady=5)

products_list.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Create GUI components for search
label_search = tk.Label(app, text="Search by Product ID:")
entry_search = tk.Entry(app)
button_search = tk.Button(app, text="Search", command=search_product)
search_result_label = tk.Label(app, text="Search Result:")
search_result_list = tk.Listbox(app, width=50, height=5)

# Arrange GUI components for search using grid layout
label_search.grid(row=9, column=0)
entry_search.grid(row=9, column=1)
button_search.grid(row=9, column=2)
search_result_label.grid(row=10, column=0, columnspan=2, pady=5)
search_result_list.grid(row=11, column=0, columnspan=2, padx=5, pady=5)


app.mainloop()

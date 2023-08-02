# products.py

# Class representing a product
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

# A list to simulate data storage (replace this with a database in a real project)
product_data_list = []

# Function to add a new product to the product_data_list
def add_product(product_id, name, price, quantity):
    product = Product(product_id, name, price, quantity)
    product_data_list.append(product)

# Function to retrieve all products
def get_all_products():
    return product_data_list

# Function to get a product by its ID
def get_product_by_id(product_id):
    for product in product_data_list:
        if product.product_id == product_id:
            return product
    return None

# Problem Statement
# You have a list of dictionaries where each dictionary represents a product with its name, price, and category. Your task is to perform the following operations using list comprehensions:

# Create a list of product names that belong to a specific category (e.g., "Electronics").
# Create a list of dictionaries with discounted prices for all products, applying a 10% discount to each.
# Create a list of product names with prices over $50.
# Create a list of tuples where each tuple contains a product name and a category for products priced under $20.

products = [
    {"name": "Laptop", "price": 999.99, "category": "Electronics"},
    {"name": "Smartphone", "price": 799.99, "category": "Electronics"},
    {"name": "Coffee Maker", "price": 19.99, "category": "Home Appliances"},
    {"name": "Book", "price": 12.99, "category": "Books"},
    {"name": "Headphones", "price": 149.99, "category": "Electronics"},
    {"name": "Blender", "price": 24.99, "category": "Home Appliances"},
    {"name": "Board Game", "price": 29.99, "category": "Toys"},
    {"name": "Chair", "price": 49.99, "category": "Furniture"},
    {"name": "Shoes", "price": 79.99, "category": "Clothing"},
    {"name": "T-shirt", "price": 9.99, "category": "Clothing"}
]

# Task 1
# Create a list of product names that belong to a specific category (e.g., "Electronics").
# Example output: ['Laptop', 'Smartphone', 'Headphones']

electronic_product = [product['name'] for product in products if product['category'] =="Electronics"]
print(electronic_product)

# Task 2
# Create a list of dictionaries with discounted prices for all products, applying a 10% discount to each.
# Example output: [{'name': 'Laptop', 'price': 899.99, 'category': 'Electronics'}, ...]

discounted_products = [{**product, "price": round(product["price"] * 0.9, 2)} for product in products]
print("Products with discounted prices:", discounted_products)

# Task 3
# Create a list of product names with prices over $50.
# Example output: ['Laptop', 'Smartphone', 'Headphones', 'Shoes']

over_price = [product["name"] for product in products if product['price']  > 50 ]
print(over_price)

# Task 4
# Create a list of tuples where each tuple contains a product name and a category for products priced under $20.
# Example output: [('Coffee Maker', 'Home Appliances'), ('Book', 'Books'), ('T-shirt', 'Clothing')]

under_price = [(product['name'], product['category']) for product in products if product['price'] < 20]
print(under_price)

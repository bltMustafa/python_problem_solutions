# Problem Statement
# You are given a list of strings representing product names and their prices separated by a colon. Your task is to use list comprehensions to perform the following tasks:

# Extract the product names and create a new list containing only the names.
# Extract the product prices and create a new list containing the prices as floats.
# Create a new list containing only the names of products priced above $20.
# Create a dictionary where the keys are the product names and the values are the product prices.

products = [
    "Apple:2.99",
    "Banana:1.49",
    "Cherry:3.99",
    "Date:5.49",
    "Elderberry:25.00",
    "Fig:22.50",
    "Grape:15.00",
    "Honeydew:10.00",
    "Iced Tea:2.50",
    "Jelly:18.00"
]

# Task 1
# Example output: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Iced Tea', 'Jelly']
# Create a list containing only the product names.
product_names = [product.split(':')[0] for product in products]
print(product_names)

# Task 2
# Example output: [2.99, 1.49, 3.99, 5.49, 25.0, 22.5, 15.0, 10.0, 2.5, 18.0]
# Create a list containing the product prices as floats.
product_value = [float(product.split(':')[1]) for product in products]
print(product_value)

# Task 3
# Example output: ['Elderberry', 'Fig']
# Create a list containing only the names of products priced above $20.

product_above = [product.split(':')[0] for product in products if float(product.split(':')[1]) > 20]
print(product_above)

# Task 4
# Example output: {'Apple': 2.99, 'Banana': 1.49, 'Cherry': 3.99, ...}
# Create a dictionary where the keys are the product names and the values are the product prices.

product_dict = {product.split(':')[0]: float(product.split(':')[1]) for product in products}
print(product_dict)




inventory = [
    {"name": "Laptop", "price": 999.99, "stock": 5},
    {"name": "Smartphone", "price": 799.99, "stock": 8},
    {"name": "Tablet", "price": 299.99, "stock": 15},
    {"name": "Headphones", "price": 199.99, "stock": 12},
    {"name": "Monitor", "price": 149.99, "stock": 7},
    {"name": "Mouse", "price": 49.99, "stock": 25},
    {"name": "Keyboard", "price": 89.99, "stock": 10},
    {"name": "USB Cable", "price": 9.99, "stock": 100},
]

# Task 1
# We calculate the total value of all products by multiplying each product's price by its stock quantity.

total_stock_value = sum(item["price"] * item["stock"] for item in inventory)
print(total_stock_value)

# Task 2
# Example output: ['Laptop', 'Smartphone', 'Monitor']
# We filter out products with a stock quantity less than 10 and add their names to a list.

stock = [product['name'] for product in inventory if product['stock'] < 10 ]
print(stock)

# Task 3
# We use the max function to find the most expensive product.
# Example output: 'Laptop'

most_expensive_product = max(inventory, key=lambda x:x["price"])['name']
print(most_expensive_product)

# Task 4
# Example output: [('Mouse', 39.99), ('USB Cable', 7.99)]
# We find products priced under 50, and return a list containing their names and their prices after applying a 20% discount.

discounted_items = [(item["name"], round(item["price"] * 0.8, 2)) for item in inventory if item["price"] < 50]
print(discounted_items)
# Problem Statement
# You have a list of tuples, where each tuple contains a person's name and their age. Your task is to perform the following operations using list comprehensions:

# Create a list of names of people who are at least 18 years old (adults).
# Create a list of tuples where each tuple contains the name and a boolean indicating whether the person is a minor (under 18).
# Create a list of names that start with the letter 'J'.
# Create a list of ages increased by 5 years.

people = [
    ("Alice", 30),
    ("Bob", 17),
    ("Charlie", 22),
    ("David", 15),
    ("Eve", 29),
    ("Frank", 12),
    ("Grace", 34),
    ("Henry", 18),
    ("Ivy", 19),
    ("Jack", 20),
    ("Jill", 16)
]

# Task 1
# Example output: ['Alice', 'Charlie', 'Eve', 'Grace', 'Henry', 'Ivy', 'Jack']
# Create a list of names of people who are at least 18 years old (adults).
adult_age = [name for name, age in people if age >= 18]
print(adult_age)

# Task 2
# Example output: [('Alice', False), ('Bob', True), ('Charlie', False), ('David', True), ...]
# Create a list of tuples where each tuple contains the name and a boolean indicating whether the person is a minor (under 18).
minor = [(name, age < 18) for name, age in people]
print(minor)

# Task 3
# Example output: ['Jack', 'Jill']
# Create a list of names that start with the letter 'J'.

first_word = [name for name, _ in people if name.startswith('J')]
print(first_word)

# Task 4
# Example output: [35, 22, 27, 20, 34, 17, 39, 23, 24, 25, 21]
# Create a list of ages increased by 5 years.
add_age = [age + 5 for _, age in people]
print(add_age)

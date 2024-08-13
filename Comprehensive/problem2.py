# Problem Statement
# You have a list of integers representing the ages of a group of people. Your task is to use list comprehensions to perform the following:

# Create a new list of ages that are even numbers.
# Create a new list containing the squares of each age.
# Create a new list of ages that are above the average age.
# Create a list of age groups, categorizing each age as "Child" (0-12), "Teen" (13-19), "Adult" (20-64), or "Senior" (65 and above).

ages = [5, 12, 17, 24, 35, 42, 51, 64, 73, 88, 95]

# Create a new list of ages that are even numbers.
even_ages = [age for age in ages if age % 2 == 0]
print(even_ages)

# Create a new list containing the squares of each age.
square_ages = [age ** 2 for age in ages]
print(square_ages)

# Create a new list of ages that are above the average age.
ages_ort = sum(ages) / len(ages)
ages_above_ort = [age for age in ages if age > ages_ort]
print(ages_above_ort)
print(ages_ort)

# Create a list of age groups, categorizing each age as "Child" (0-12), "Teen" (13-19), "Adult" (20-64), or "Senior" (65 and above).
age_groups = [
    "Child" if age <= 12 else
    "Teen" if 13 <= age <= 19 else
    "Adult" if 20 <= age <= 64 else
    "senior"
    for age in ages
]

print(age_groups)
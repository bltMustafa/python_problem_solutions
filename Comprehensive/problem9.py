# 1. List the names of students who scored 80 or above.
# 2. Create a new list by increasing all students' grades by 10% (but not exceeding 100).
# 3. Create a list of tuples containing the names and ages of students aged 21 and above.
# 4. Filter out students who scored below 70 and list only their names.

students = [
    {"name": "Ali", "age": 20, "grade": 85},
    {"name": "Zeynep", "age": 22, "grade": 92},
    {"name": "Mehmet", "age": 21, "grade": 76},
    {"name": "Ayse", "age": 23, "grade": 89},
    {"name": "Can", "age": 19, "grade": 95},
    {"name": "Elif", "age": 20, "grade": 65},
]

# 1. List the names of students with grades 80 or above
successful_students = [student["name"] for student in students if student["grade"] >= 80]
print(successful_students)

# 2. Increase all students' grades by 10%, ensuring the grade does not exceed 100
updated_students = [
    {**student, "grade": min(student["grade"] * 1.1, 100)} for student in students
]
print(updated_students)

# 3. List the names and ages of students who are 21 years old or older
older_students = [(student['name'], student['age']) for student in students if student["age"] >= 21]
print(older_students)

# 4. List the names of students who scored below 70
low_grade_students = [student['name'] for student in students if student['grade'] < 70]
print(low_grade_students)

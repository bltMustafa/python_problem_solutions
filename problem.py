students = [
    {"name": "Alice", "Mathematics": 85, "Science": 82, "English": 88},
    {"name": "Bob", "Mathematics": 78, "Science": 75, "English": 80},
    {"name": "Charlie", "Mathematics": 90, "Science": 92, "English": 85},
    {"name": "David", "Mathematics": 68, "Science": 74, "English": 75},
    {"name": "Eve", "Mathematics": 95, "Science": 94, "English": 99},
]

# Students Scoring Above 80 in All Subjects:
# Create a list of names of students who scored more than 80 in all three subjects.
# Students Scoring Above 80 in All Subjects:
# Example output: ['Alice', 'Charlie', 'Eve']

high_scorers = [student["name"] for student in students if student["Mathematics"] > 80 and student["Science"] > 80 and student["English"] > 80]
print(high_scorers)


# List of Student Names and Their Average Scores:
# Create a list of dictionaries, each containing the student's name and their average score across all subjects.
# Example output: [{'name': 'Alice', 'average': 85.0}, {'name': 'Bob', 'average': 77.67}, ...]
average_score = [{'name': student['name'], 'average': (student["Mathematics"] + student["Science"] + student["English"])/3} for student in students]
print(average_score)


# Example output: ['Charlie', 'Eve']
# Students with average score above 85
# Task 3: It filters the students from the average_scores list whose average score is greater than 85.
about_average_student = [student["name"] for student in average_score if student["average"] > 85]
print(about_average_student)




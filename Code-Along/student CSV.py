students = [
    {"name": "adam", "class": "AI23", "email": "adam@gmail.com"},
    {"name": "kalle", "class": "AI23", "email": "kalle@gmail.com"},
    {"name": "eva", "class": "AI22", "email": "eva@gmail.com"},
]

print(students)

with open("..\\data\\students.csv", "w") as file:
    for student in students:
        file.write(f"{student['name']}, {student['class']}, {student['email']}\n")

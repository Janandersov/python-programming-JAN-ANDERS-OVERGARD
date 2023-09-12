import csv

students = []

with open("..\\data\\students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append({"name": row["name"], "class": row["class"], "email": row["email"]})

print(students)

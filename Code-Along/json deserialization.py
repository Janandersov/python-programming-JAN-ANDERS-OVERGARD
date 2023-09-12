import json

with open("..\\data\\teacher.json", "r") as file:
    data = file.read()

teacher = (json.loads(data))

print(teacher)
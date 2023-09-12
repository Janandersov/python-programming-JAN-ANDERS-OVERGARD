import json

teacher = {
    "firstname": "Fredrik",
    "lastname": "Johansson",
    "age": 42,
    "languages": ["Python", "C#", "Javascript"],
    "contactinfo": {
        "phone": "0702345678",
        "email": [
            "fredrik@everyloop.com",
            "fredrik@gmail.com",
            "fredrik.johansson@hotmail.com",
        ]
    }
}

serialized_data = json.dumps(teacher, indent=4)

# print(serialized_data)

with open("..\\data\\teacher.json", "w") as file:
    file.write(serialized_data)

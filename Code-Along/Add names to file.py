with open("..\\data\\names.txt", "r") as file:
    name_list = [name.strip("\n") for name in file.readlines()]

while True:
    new_name = input("Enter a name: ")
    if not new_name:
        break
    name_list.append(new_name)

print(name_list)

for name in name_list:
    print(name)

with open("../data\\names.txt", "w") as file:
    file.writelines(name + "\n" for name in name_list)

print("Names are saved!")

list_with_colors = []

user_input = input("Please write a color to be added to the list: ")

while user_input != "":
    list_with_colors.append(user_input)
    user_input = input("Please write another color or press enter to print out the list: ")

print(list_with_colors)
print(len(list_with_colors))

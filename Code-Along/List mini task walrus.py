list_with_colors = []

while (user_input := input("Please write a color to be added to the list: ")) and user_input != "":
    list_with_colors.append(user_input)

print(list_with_colors)
print(len(list_with_colors))

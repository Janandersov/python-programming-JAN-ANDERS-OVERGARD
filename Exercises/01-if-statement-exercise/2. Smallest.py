print("Welcome to the smallest number checker!\n")
first_number = float(input("Please input the FIRST number: "))
second_number = float(input("Please input the SECOND number: "))

# using g (General format) in the f-string formatting removes decimal spaces if the input number is a whole number
if first_number < second_number:
    print(f"The first number you typed: {first_number:g}, is the smallest one!")
elif first_number > second_number:
    print(f"The second number you typed: {second_number:g}, is the smallest one!")
else:
    print(f"Your two numbers ({first_number:g}), are equal!")

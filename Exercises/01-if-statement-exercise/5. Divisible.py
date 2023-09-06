print("Welcome to the number checker!\n")

user_number = int(input("Please input a whole number: "))

if user_number % 2 == 0:
    if user_number % 5 == 0:
        print("\nYour number is even and divisible by 5.")
    else:
        print("\nYour number is even but not divisible by 5.")

else:
    if user_number % 5 == 0:
        print("\nYour number is odd and divisible by 5.")
    else:
        print("\nYour number is odd but not divisible by 5.")

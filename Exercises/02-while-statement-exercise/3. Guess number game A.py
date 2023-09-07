import random

random_number = random.randint(1, 100)
number_of_tries = 1

guessed_number = float(input("Please guess a whole number between 1 and 100: "))

while guessed_number != random_number:
    if guessed_number > random_number:
        print("\nYour guessed number is too high.")
    else:
        print("\nYour guessed number is too low.")
    number_of_tries += 1
    guessed_number = float(input("Please guess another number: "))

print(f"\nCongratulations! You guessed the number {random_number} in {number_of_tries} tries!")

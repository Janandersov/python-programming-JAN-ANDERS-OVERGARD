import random

random_number = random.randint(1, 100)
number_of_tries = 0
lowest_number = 1
highest_number = 100
    
while True:
    algorithm_guess = (lowest_number + highest_number) // 2
    number_of_tries += 1

    if algorithm_guess == random_number:
        print(f"\nCongratulations! You guessed the correct number {random_number} in {number_of_tries} tries.")
        break
    elif algorithm_guess > random_number:
        print(f"\nNumber {algorithm_guess} is too high. This was try number {number_of_tries}.")
        highest_number = algorithm_guess - 1
    else:
        print(f"\nNumber {algorithm_guess} is too low. This was try number {number_of_tries}.")
        lowest_number = algorithm_guess + 1

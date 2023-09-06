print("Welcome to the medicine amount recommender.\n")

user_age = int(input("Please state your age in WHOLE years: "))
user_weight = int(input("Please state your weight in WHOLE kilograms: "))

# A bit confused by the "for children weight is more important than age" part.
# Decided to read it as if a child 3-12 years happens to be over 40kg it should take 1-2 pills.
# I do understand what to do if the task means that above 40kg is always adolescent.

if user_age < 3 or user_weight < 15:
    print("\nSorry, you do not meet the requirements to take this medicine")
elif 3 <= user_age <= 12:
    if 15 <= user_weight <= 25:
        print("\nTake 1/2 pill.")
    elif 26 <= user_weight <= 40:
        print("\nTake 1/2 - 1 pill.")
    else:
        print("\nTake 1 - 2 pills.")
else:
    print("\nTake 1 - 2 pills.")

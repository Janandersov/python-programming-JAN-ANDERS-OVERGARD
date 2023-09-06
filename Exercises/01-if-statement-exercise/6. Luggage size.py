print("Welcome to Jan-Air, please be ready with your luggage info.\n")

luggage_weight = float(input("What is the weight of your luggage? (kg): "))
luggage_length = float(input("What is the length of your luggage? (cm): "))
luggage_width = float(input("What is the width of your luggage? (cm): "))
luggage_height = float(input("What is the height of your luggage? (cm): "))

if luggage_weight <= 8:
    if luggage_length <= 55 and luggage_width <= 40 and luggage_height <= 23:
        print("\nYour luggage is allowed on board, have a nice flight!")
    else:
        print("\nUnfortunately your luggage is above the size limit (55x40x23cm).")
else:
    print("\nUnfortunately your luggage is above the weight limit (8kg).")

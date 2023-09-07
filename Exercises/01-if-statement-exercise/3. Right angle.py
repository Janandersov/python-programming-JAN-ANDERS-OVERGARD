print("Welcome to the tri-angular-calculator!\n")
first_angle = float(input("Please input the FIRST angle of your triangle: "))
second_angle = float(input("Please input the SECOND angle of your triangle: "))
third_angle = float(input("Please input the THIRD angle of your triangle: "))

if first_angle + second_angle + third_angle != 180:
    print("\nSorry, those angles does not make a valid triangle.")
elif first_angle <= 0 or second_angle <= 0 or third_angle <= 0:
    print("\nSorry, you can not make a valid triangle if an angle is zero degrees or less.")
elif first_angle == 90 or second_angle == 90 or third_angle == 90:
    print("\nYour triangle has a right angle!")
else:
    print("\nYour triangle does not have a right angle.")

import random

dice_roll_values = []

for i in range(10):
    dice_roll = random.randint(1, 6)
    dice_roll_values.append(dice_roll)

dice_roll_values.sort(reverse=True)
print(dice_roll_values)
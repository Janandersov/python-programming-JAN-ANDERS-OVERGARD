import math

x_1 = 2
y_1 = 1
z_1 = 4

x_2 = 3
y_2 = 1
z_2 = 0

line_length = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2 + (z_2 - z_1) ** 2)

print(f"The distance between the points is around{line_length: .2f} length units.")

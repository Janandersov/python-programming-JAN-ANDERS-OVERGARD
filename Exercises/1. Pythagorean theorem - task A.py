import math

cathetus_a = 3
cathetus_b = 4

cathetus_a_squared = cathetus_a ** 2
cathetus_b_squared = cathetus_b ** 2

hypotenuse_squared = cathetus_a_squared + cathetus_b_squared

hypotenuse = math.sqrt(hypotenuse_squared)

print(f"The hypotenuse is{hypotenuse: .0f} length units!")

import math

hypotenuse_c = 7.0
cathetus_a = 5.0

hypotenuse_c_squared = hypotenuse_c ** 2
cathetus_a_squared = cathetus_a ** 2

cathetus_b_squared = hypotenuse_c_squared - cathetus_a_squared

cathetus_b = math.sqrt(cathetus_b_squared)

print(f"Cathetus b is{cathetus_b: .1f} length units!")


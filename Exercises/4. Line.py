x_a = 4
y_a = 4
x_b = 0
y_b = 1

value_k = (y_b - y_a) / (x_b - x_a)

value_m = y_a - value_k * x_a

print(f"k ={value_k: .2f} and m ={value_m: .0f}. The equation for the slope is y ={value_k: .2f}x +{value_m: .0f}.")

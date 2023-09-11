import matplotlib.pyplot as plt

x = list(range(-10, 11))
y = [value ** 2 for value in x]
y2 = [value ** 3 for value in x]

print(f"{x= }")
print(f"{y= }")

plt.title("My graph")
plt.xlabel("X-values")
plt.ylabel("Y-values")
plt.plot(x, y, label="x**2", color="red", linestyle="dotted", marker="o")
plt.plot(x, y2, label="x**3", color="blue", linestyle="solid", marker=".")
plt.legend(loc="best")
plt.show()

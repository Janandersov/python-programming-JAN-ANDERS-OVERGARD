import matplotlib.pyplot as plt

range_list = list(range(-10, 11))
squared_list = [i ** 2 for i in range_list]

plt.plot(squared_list)
plt.show()
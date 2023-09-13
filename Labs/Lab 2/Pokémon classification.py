import matplotlib.pyplot as plt

pichu_list = []
pichu_width = []
pichu_height = []

pikachu_list = []
pikachu_width = []
pikachu_height = []

with open("data\\datapoints.txt") as file:
    datapoints = file.readlines()[1:]

for line in datapoints:
    width, height, label = line.strip().split(", ")
    datapoints_dict = {"width": width, "height": height, "label": label}
    if datapoints_dict["label"] == "0":
        pichu_list.append(datapoints_dict)
        pichu_width.append(width)
        pichu_height.append(height)
    else:
        pikachu_list.append(datapoints_dict)
        pikachu_width.append(width)
        pikachu_height.append(height)

plt.scatter(pichu_width, pichu_height, color="red")
plt.scatter(pikachu_width, pikachu_height, color="blue")
plt.show()

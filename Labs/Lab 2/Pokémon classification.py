import math
import matplotlib.pyplot as plt

# Initialize lists for datapoints and testpoints.
pichu_width = []
pichu_height = []

pikachu_width = []
pikachu_height = []

test_width = [25, 24.2, 22, 20.5]
test_height = [32, 31.5, 34, 34]

# Read datapoints.txt and split data into correct lists.
with open("data\\datapoints.txt") as file:
    datapoints = file.readlines()[1:]

for line in datapoints:
    width, height, label = line.strip().split(", ")
    datapoints_dict = {"width": width, "height": height, "label": label}
    if datapoints_dict["label"] == "0":
        pichu_width.append(width)
        pichu_height.append(height)
    else:
        pikachu_width.append(width)
        pikachu_height.append(height)

# Create scatterplot for each set of lists and displays them in different colors.
plt.scatter(pichu_width, pichu_height, color="red")
plt.scatter(pikachu_width, pikachu_height, color="blue")
plt.show()

# Looping trough test points.
for x in range(len(test_width)):
    # Variables tracks the smallest distance between points.
    smallest_pichu = float("inf")
    smallest_pikachu = float("inf")

    # Calculates distances to Pichu datapoints.
    for y in range(len(pichu_width)):
        pichu_point_distance = math.sqrt(
            (test_width[x] - float(pichu_width[y])) ** 2 + (test_height[x] - float(pichu_height[y])) ** 2)
        smallest_pichu = min(smallest_pichu, pichu_point_distance)

    # Calculates distances to Pikachu datapoints.
    for y in range(len(pikachu_width)):
        pikachu_point_distance = math.sqrt(
            (test_width[x] - float(pikachu_width[y])) ** 2 + (test_height[x] - float(pikachu_height[y])) ** 2)
        smallest_pikachu = min(smallest_pikachu, pikachu_point_distance)

    # Compares distance to Pichu vs. Pikachu and prints the classification.
    if smallest_pichu < smallest_pikachu:
        print(f"Sample with (width, height): ({test_width[x]}, {test_height[x]}) classified as Pichu")
    else:
        print(f"Sample with (width, height): ({test_width[x]}, {test_height[x]}) classified as Pikachu")

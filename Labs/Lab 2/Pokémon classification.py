import math
import matplotlib.pyplot as plt


# Main function, runs first.
def main():
    print("Welcome to the pokemon classifier!\n")
    sort_datapoints()
    main_menu()


def main_menu():
    print("What do you want to do?")
    print("1. Classify using testdata.")
    print("2. Classify using your own data.")
    print("3. Show the training datapoints in a scatterplot.")

    while True:
        try:
            user_choice = int(input("Make your choice (1-3): "))
            print()
            if 3 >= user_choice >= 1:
                if user_choice == 1:
                    sort_testpoints()
                elif user_choice == 2:
                    user_defined_points()
                else:
                    plot_points()

                return
        except ValueError:
            pass
        print("You have to make a valid choice.")


def sort_datapoints():
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


def sort_testpoints():
    # Read testpoints.txt and split data into correct lists.
    with open("data\\testpoints.txt", "r") as file:
        testpoints = file.readlines()[1:]

    for line in testpoints:
        clean_line = line.split(". ")[1].strip("()\n")
        width, height = map(float, clean_line.split(", "))
        test_width.append(width)
        test_height.append(height)
    # Runs classification with testpoints.
    distance_between_points(test_width, test_height)


def user_defined_points():
    # Taking user input and appending to correct lists.
    while True:
        try:
            width = float(input("Please input Pokemon width: "))
            height = float(input("Please input Pokemon height: "))
            if width > 0 and height > 0:
                test_width.append(width)
                test_height.append(height)
                # Runs classification with user defined points.
                distance_between_points(test_width, test_height)
                return
        except ValueError:
            pass
        print("You have to use positive numbers for width and height.")


def distance_between_points(width_list, height_list):
    # Looping trough test points.
    for x in range(len(width_list)):
        # Lists tracks the smallest distances between points.
        distances_to_pichu = []
        distances_to_pikachu = []

        # Calculates distances to Pichu datapoints and appends to list.
        for y in range(len(pichu_width)):
            pichu_point_distance = math.sqrt(
                (width_list[x] - float(pichu_width[y])) ** 2 + (height_list[x] - float(pichu_height[y])) ** 2)
            distances_to_pichu.append(pichu_point_distance)

        # Calculates distances to Pikachu datapoints and appends to list.
        for y in range(len(pikachu_width)):
            pikachu_point_distance = math.sqrt(
                (width_list[x] - float(pikachu_width[y])) ** 2 + (height_list[x] - float(pikachu_height[y])) ** 2)
            distances_to_pikachu.append(pikachu_point_distance)

        # Sorts both distance lists and takes the 10 closest points
        ten_closest_pichu = sorted(distances_to_pichu)[:10]
        ten_closest_pikachu = sorted(distances_to_pikachu)[:10]

        # Counts the number of closest points for pichu/pikachu
        closest_to_pichu = sum(1 for distance in ten_closest_pichu if distance < min(ten_closest_pikachu))
        closest_to_pikachu = sum(1 for distance in ten_closest_pikachu if distance < min(ten_closest_pichu))

        # Checks if pichu or pikachu has the most points and classifies based on that.
        if closest_to_pichu > closest_to_pikachu:
            print(f"Sample with (width, height): ({width_list[x]}, {height_list[x]}) classified as Pichu")
        else:
            print(f"Sample with (width, height): ({width_list[x]}, {height_list[x]}) classified as Pikachu")

    # Clearing lists with test points.
    test_width.clear()
    test_height.clear()


def plot_points():
    # Create scatterplot for each set of lists and displays them in different colors.
    plt.scatter(pichu_width, pichu_height, color="red")
    plt.scatter(pikachu_width, pikachu_height, color="blue")
    plt.show()


# Initialize lists for datapoints and testpoints.
pichu_width = []
pichu_height = []

pikachu_width = []
pikachu_height = []

test_width = []
test_height = []

# Run main function
main()

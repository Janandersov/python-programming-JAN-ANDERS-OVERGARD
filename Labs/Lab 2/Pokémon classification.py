import math
import matplotlib.pyplot as plt


def main():
    # Main function, runs first.
    print("Welcome to the pokemon classifier!\n")
    sort_datapoints()
    main_menu()


def main_menu():
    # Main menu for the user to choose what to do.
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
                    return_or_end()
                elif user_choice == 2:
                    user_defined_points()
                    return_or_end()
                else:
                    plot_points()
                    return_or_end()

                return
        except ValueError:
            pass
        print("You have to make a valid choice.")


def sort_datapoints():
    # Read datapoints.txt and split/append data into correct lists.
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
    # Read testpoints.txt and split/append data into correct lists.
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
        # List to track the distances between points.
        distances_to_testpoint = []

        # Calculates distances to Pichu datapoints and appends to list with label Pichu.
        for y in range(len(pichu_width)):
            pichu_point_distance = math.sqrt(
                (width_list[x] - float(pichu_width[y])) ** 2 + (height_list[x] - float(pichu_height[y])) ** 2)
            distances_to_testpoint.append((pichu_point_distance, "Pichu"))

        # Calculates distances to Pikachu datapoints and appends to list with label Pikachu.
        for y in range(len(pikachu_width)):
            pikachu_point_distance = math.sqrt(
                (width_list[x] - float(pikachu_width[y])) ** 2 + (height_list[x] - float(pikachu_height[y])) ** 2)
            distances_to_testpoint.append((pikachu_point_distance, "Pikachu"))

        # Sorts the list with distances and takes the 10 closest points.
        ten_closest_points = sorted(distances_to_testpoint)[:10]

        # Counts the number of closest points for pichu/pikachu
        count_pichu = sum(1 for distance, label in ten_closest_points if label == "Pichu")
        count_pikachu = sum(1 for distance, label in ten_closest_points if label == "Pikachu")

        # Checks if pichu or pikachu has the most points and classifies based on that.
        if count_pichu > count_pikachu:
            print(f"Sample with (width, height): ({width_list[x]}, {height_list[x]}) classified as Pichu")
        else:
            print(f"Sample with (width, height): ({width_list[x]}, {height_list[x]}) classified as Pikachu")

    # Clearing lists with test points.
    test_width.clear()
    test_height.clear()


def plot_points():
    # Create scatterplot for each set of lists and displays them in different colors.
    plt.scatter([float(w) for w in pichu_width], [float(h) for h in pichu_height], color="red", label="Pichu")
    plt.scatter([float(w) for w in pikachu_width], [float(h) for h in pikachu_height], color="blue", label="Pikachu")
    plt.legend()
    plt.xlabel("Width (cm)")
    plt.ylabel("Height (cm)")
    plt.title("Pokemon Classification")
    plt.show()


def return_or_end():
    # Menu for going back to main menu or exit.
    print("\nDo you want to return to the main menu or exit the program?")
    print("1. Return to main menu.")
    print("2. Exit.")

    while True:
        try:
            user_choice = int(input("Make your choice (1-2): "))
            print()
            if 2 >= user_choice >= 1:
                if user_choice == 1:
                    main()
                else:
                    exit()

                return
        except ValueError:
            pass
        print("You have to make a valid choice.")


# Initialize lists for datapoints and testpoints.
pichu_width = []
pichu_height = []

pikachu_width = []
pikachu_height = []

test_width = []
test_height = []

# Run main function
main()

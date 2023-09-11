user_name = str(input("Please enter your first and last name: "))
split_names = user_name.split()
middle_names = ' '.join(split_names[1:-1])

if len(split_names) >= 3:
    print(f"First name: {split_names[0]}")
    print(f"Middle name(s): {middle_names}")
    print(f"Last name: {split_names[-1]}")
else:
    print(f"First name: {split_names[0]}")
    print(f"Last name: {split_names[-1]}")


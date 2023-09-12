file = open("..\Data\hello.txt", "a")

new_content = input("Enter text: ")

file.writelines("\n" + new_content)

file.close()

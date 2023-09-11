user_word = str(input("Please type a word: "))
upper_count = sum(letter.isupper() for letter in user_word)
lower_count = sum(letter.islower() for letter in user_word)

print(f"Your word has {upper_count} uppercase letter(s) and {lower_count} lowercase letter(s).")

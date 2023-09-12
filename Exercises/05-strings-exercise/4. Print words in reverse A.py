user_sentence = str(input("Please write a sentence: "))
word_list = user_sentence.split()[::-1]

print(" ".join(word_list))

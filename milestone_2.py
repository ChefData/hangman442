import random

word_list = ["Mango", "Pineapple", "Mangosteen", "Lychee", "Fig"]
print(word_list)

random_word = random.choice(word_list)
print(random_word)

letter_guess = input("Enter a single letter: ")
if len(letter_guess) == 1 and letter_guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")


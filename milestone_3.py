import random

word_list = ["Mango", "Pineapple", "Mangosteen", "Lychee", "Fig"]
random_word = random.choice(word_list)

while True:
    letter_guess = input("Enter a single letter: ")
    if len(letter_guess) == 1 and letter_guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")


if letter_guess in random_word:
    print(f"Good guess! {letter_guess} is in the word.")
else:
    print(f"Sorry, {letter_guess} is not in the word. Try again.")
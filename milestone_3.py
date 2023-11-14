import random

word_list = ["Mango", "Pineapple", "Mangosteen", "Lychee", "Fig"]
random_word = random.choice(word_list)

def check_guess(guess):
    lower_case_guess = guess.lower()
    if lower_case_guess in random_word:
        print(f"Good guess! {lower_case_guess} is in the word.")
    else:
        print(f"Sorry, {lower_case_guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        letter_guess = input("Enter a single letter: ")
        if len(letter_guess) == 1 and letter_guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(letter_guess)

ask_for_input()
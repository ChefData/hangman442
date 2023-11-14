while True:
    letter_guess = input("Enter a single letter: ")
    if len(letter_guess) == 1 and letter_guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
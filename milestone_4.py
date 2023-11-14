import random

# word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
# word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
# num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
# num_lives: int - The number of lives the player has at the start of the game.
# word_list: list - A list of words
# list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        lower_case_guess = guess.lower()
        if lower_case_guess in self.word:
            print(f"Good guess! {lower_case_guess} is in the word.")
            for char in range(len(self.word)):
                if self.word[char] == lower_case_guess:
                    self.word_guessed[char] = lower_case_guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {lower_case_guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            letter_guess = input("Enter a single letter: ")
            if not letter_guess.isalpha() or len(letter_guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif letter_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(letter_guess)
                self.list_of_guesses.append(letter_guess)
                break 

word_list = ["Mango", "Pineapple", "Mangosteen", "Lychee", "Fig"]
hangman_game = Hangman(word_list)
hangman_game.ask_for_input()
print(f"List of guesses: {hangman_game.list_of_guesses}")
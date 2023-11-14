import random
from urllib.request import urlopen

# word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
# word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
# num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
# num_lives: int - The number of lives the player has at the start of the game.
# word_list: list - A list of words
# list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially

class Hangman:

    num_lives = int(input("How many lives would you like? "))

    def __init__(self, word_list):
        self.word_list = word_list
        self.num_lives = self.__class__.num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []

    def check_guess(self, guess):
        lower_case_guess = guess.lower()
        lower_case_word = self.word.lower()
        if lower_case_guess in lower_case_word:
            print(f"Good guess! {lower_case_guess} is in the word.")
            print(f"You still have {self.num_lives} lives left.")
            for char in range(len(lower_case_word)):
                if lower_case_word[char] == lower_case_guess:
                    self.word_guessed[char] = lower_case_guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {lower_case_guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            letter_guess = input("Enter a single letter: ")
            if not letter_guess.isalpha() or len(letter_guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif letter_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(letter_guess)
                self.list_of_guesses.append(letter_guess)
                break 

def play_game(word_list):
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            print(f"The correct word was: {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            print(f"Letters guessed: {', '.join(set(game.list_of_guesses))}")
            print(f"Incorrect guesses: {', '.join(set(game.list_of_guesses) - set(game.word_guessed))}")
            print(f"Correct letters: {' '.join(game.word_guessed)}")
        else:
            print(f"Congratulations. You won the game! The correct word was: {game.word}")
            break

word_site = urlopen("https://www.mit.edu/~ecprice/wordlist.10000")
word_list = word_site.read().decode().splitlines()

play_game(word_list)
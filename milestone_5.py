import random
from urllib.request import urlopen

# word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
# word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
# num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
# num_lives: int - The number of lives the player has at the start of the game.
# word_list: list - A list of words
# list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially

class Hangman:

    while True:
        num_lives = input("How many lives would you like? ")
        if not num_lives.isdigit():
            print("\nInvalid number. Please, enter a number.")
        else:
            num_lives = int(num_lives)
            break 

    def __init__(self, word_list):
        self.word_list = word_list
        self.num_lives = self.__class__.num_lives
        self.word = random.choice(self.word_list).lower()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            print(f"You still have {self.num_lives} lives left.")
            for char in range(len(self.word)):
                if self.word[char] == guess:
                    self.word_guessed[char] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            letter_guess = input("\nEnter a single letter: ").lower()
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
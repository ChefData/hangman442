import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # self.word = self._choose_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

# word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
# word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
# num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
# num_lives: int - The number of lives the player has at the start of the game.
# word_list: list - A list of words
# list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially


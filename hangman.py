import random
from urllib.request import urlopen


class Hangman:
    '''
    Hangman game class.
    
    Args:
        word_list (list): List of words to choose from.

    Attributes:
        word_list (list): List of words to choose from.
        num_lives (int): Number of lives the player starts with.
        word (str): The word to guess.
        word_guessed (list): List representing the current state of guessed letters in the word.
        num_letters (int): Number of letters remaining to guess.
        list_of_guesses (list): List of letters guessed by the player.
    '''
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

    def display_final_message(self, is_winner):
        """
        Display the final message based on whether the player won or lost.

        Args:
            is_winner (bool): True if the player won, False otherwise.
        """
        if is_winner:
            print(f"\nCongratulations. You won the game! The correct word was: {self.word}")
        else:
            print("\nYou lost!")
            print(f"The correct word was: {self.word}")

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word and update the game state accordingly.

        Args:
            guess (str): The letter guessed by the player.
        """
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
        """
        Get a valid letter guess from the player and update the game state.
        """
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
    """
    Play the Hangman game.

    Args:
        word_list (list): List of words to choose from.
    """
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            game.display_final_message(is_winner=False)
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            print(f"Letters guessed: {', '.join(set(game.list_of_guesses))}")
            print(f"Incorrect guesses: {', '.join(set(game.list_of_guesses) - set(game.word_guessed))}")
            print(f"Correct letters: {' '.join(game.word_guessed)}")
        else:
            game.display_final_message(is_winner=True)
            break

def get_word_list():
    """
    Fetch and return a list of words from a URL.

    Returns:
        list: List of words.
    """
    with urlopen("https://www.mit.edu/~ecprice/wordlist.10000") as word_site:
        return word_site.read().decode().splitlines()

if __name__ == "__main__":
    word_list = get_word_list()
    play_game(word_list)
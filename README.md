# Hangman

## Table of Contents

- [Description of the project](#description-of-the-project)
  - [What the project does](#what-the-project-does)
  - [Aim of the project](#aim-of-the-project)
  - [Lessons learned](#lessons-learned)
- [Installation instructions](#installation-instructions)
- [Usage instructions](#usage-instructions)
- [File structure of the project](#file-structure-of-the-project)
- [Tools Used](#tools-used)

## Description of the project

Hangman is a classic game in which a player thinks of a word, and the other player tries to guess that word within a certain amount of attempts.

This project implements the Hangman game, where the computer thinks of a word, and the user tries to guess it.

### What the project does

This project requires the programmer to:
    1. Set up the environment
    2. Create the variables for the game
    3. Check if the guessed character is in the word
    4. Create the game class
    5. Code the logic of the game
    6. Refactor and optimise the code
    7. Document the experince

### Aim of the project

The aim of this project is to test my knowledge in the python programming language, in git and GitHub, and the command interface. The project is designed to challenge me to refactor and optimise the code, while documenting my experince.

### Lessons learned

- Created a list and assigned the list to a variable
- Imported the module random and used the random.choice method on the list to generate a new variable
- Asked the user for an input and checked the validaty of the input using the `len()` function and `.isalpha` method
- Used an if statement to communcate validaty of input back to the user
- Updated the GitHub repository with the latest code changes from your local project
- Refactored and optimised code to inculde meaningfull names and eliminate code duplication
- Created a while loop to continuously ask for user input if input was entered incorrectly
- Defined functions to abstract code
- Created a class to encapsulate the code
- Initiated the following attributes
  - word: The word to be guessed, picked randomly from the word_list.
  - word_guessed: list - A list of the letters of the word, with `_` for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be `['_', '_', '_', '_', '_']`. If the player guesses `a`, the list would be `['a', '_', '_', '_', '_']`
  - num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
  - num_lives: int - The number of lives the player has at the start of the game.
  - word_list: list - A list of words
  - list_of_guesses: list - A list of the guesses that have already been tried. Set to an empty list initially
- Used an if statement that checks if the guess is in the word
- Extended an if statement to include an elif statment that checks if the guess is already in the list_of_guesses
- Used the .append() method to append the guess to the list_of_guesses
- Used a for-loop to replace the underscore(s) in the word_guessed with the letter guessed by the user
- Extended an if statment to include an else statment that defines what happens if the guess is not in the word
- Create an instance of the class

## Installation instructions

### Windows

1. Install [Git](https://git-scm.com/download/win).
2. Open the command prompt or Git Bash.
3. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/ChefData/hangman442
    ```

### macOS

1. Open the Terminal.
2. If you don't have Git installed, you can install it using [Homebrew](https://brew.sh/):

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew install git
    ```

3. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/ChefData/hangman442
    ```

### Linux

1. Open the terminal.
2. Install Git:
    - On Ubuntu or Debian-based systems:

        ```bash
        sudo apt-get update
        sudo apt-get install git
        ```

    - On Fedora:

        ```bash
        sudo dnf install git
        ```

3. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/ChefData/hangman442
    ```

## Usage instructions

1. Navigate to the project directory:

    ```bash
    cd hangman442
    ```

2. Run the Hangman game script:

    ```bash
    python hangman.py
    ```

3. Follow the on-screen instructions to play the game.

## File structure of the project

The project is built around 4 milestone python files which increase in complexity to reach the finished game

```bash
.
├── README.md
├── __pycache__
└── hangman.py
```

## Tools Used

- Python: Programming language used for the game logic.
- Git: Version control system for tracking changes in the project.
- GitHub: Hosting platform for version control and collaboration.
- Visual Studio Code: Code editor used for development.
- URL ("<https://www.mit.edu/~ecprice/wordlist.10000>"): Word list used to populate the project
- AiCore: Educational programme for tasks and milestones used for development progression

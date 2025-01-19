# Hangman Game in Python

A simple yet engaging implementation of the classic **Hangman** game in Python. This project allows a player to guess letters and attempt to figure out a hidden word, all while trying to avoid "hanging" by exceeding the maximum number of incorrect guesses.

## Features
- **Random Word Selection**: The game randomly selects a word from a predefined list.
- **User Interaction**: Players input guesses and receive feedback on whether the guess was correct or incorrect.
- **Interactive Gameplay**: The game displays the number of incorrect guesses left and the current progress of the word with underscores representing unguessed letters.
- **Hangman Drawing**: As incorrect guesses accumulate, the game visually represents the hangman drawing.
- **Game Over Conditions**: The game ends when either the player guesses the word or runs out of attempts.

## How to Play
1. The game will prompt you with a series of underscores representing the letters of a word.
2. You can guess one letter at a time.
3. Incorrect guesses will decrease the number of remaining attempts.
4. The game ends if you either guess all the letters of the word correctly or run out of attempts.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/hangman-python.git
    ```
2. Navigate into the project directory:
    ```bash
    cd hangman-python
    ```
3. Run the game:
    ```bash
    python hangman.py
    ```

## Contributing
Feel free to fork the repository, create a branch, and submit pull requests with improvements, bug fixes, or new features!


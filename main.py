import random
import tkinter as tk
from tkinter import messagebox
from hangman_words import word_list  # Ensure this file is available with word_list
from hangman_art import stages, logo  # Ensure this file is available with stages and logo

# Debugging: Print the contents of logo and stages
print("Logo:", logo)  # Ensure logo is a string
print("Stages:", stages)  # Ensure stages is a list of strings

# Function to start a new game
def new_game():
    global lives, chosen_word, word_length, placeholder, correct_letters, game_over
    lives = 6
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    placeholder = " _ " * word_length
    correct_letters = []
    game_over = False

    # Update the display elements
    word_label.config(text="Word to guess: " + placeholder)
    lives_label.config(text=f"Lives left: {lives}")
    hangman_canvas.config(text=stages[lives])

    # Clear the input field
    guess_entry.delete(0, tk.END)

    print("New game started!")

# Set up the game (initial game state)
lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
placeholder = " _ " * word_length
correct_letters = []
game_over = False

# Create the main window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("600x500")  # Increased window size to ensure everything fits
root.configure(bg="#000000")  # Set background color to black

# Create and display the logo
logo_label = tk.Label(root, text=logo, font=("Courier", 16), bg="#000000", justify="center", fg="white")
logo_label.pack(pady=20)

# Create a label to display the word placeholder
word_label = tk.Label(root, text="Word to guess: " + placeholder, font=("Courier", 14), bg="#000000", fg="white")
word_label.pack(pady=10)

# Create a label to display the number of lives
lives_label = tk.Label(root, text=f"Lives left: {lives}", font=("Courier", 14), bg="#000000", fg="white")
lives_label.pack(pady=10)

# Create a label to display the hangman stages
hangman_canvas = tk.Label(root, text=stages[lives], font=("Courier", 14), bg="#000000", fg="white", justify="center")
hangman_canvas.pack(pady=20)

# Function to update the display
def update_display():
    global placeholder, lives
    display = ""

    # Generate the current display string for the word
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Update the labels
    word_label.config(text="Word to guess: " + display)
    lives_label.config(text=f"Lives left: {lives}")
    hangman_canvas.config(text=stages[lives])

    # Check for win or lose conditions
    if "_" not in display:
        messagebox.showinfo("You Win", "Congratulations! You've guessed the word!")
        return True
    elif lives == 0:
        messagebox.showinfo("You Lose", f"Game Over! The word was {chosen_word}.")
        return True

    return False

# Function to handle the user's guess
def guess_letter():
    global lives, game_over, correct_letters
    guess = guess_entry.get().lower()

    if guess in correct_letters:
        messagebox.showinfo("Info", f"You've already guessed {guess}")
        return

    if guess not in chosen_word:
        lives -= 1
        messagebox.showinfo("Incorrect Guess", f"You guessed {guess}, that's not in the word.")

    correct_letters.append(guess)

    # Update the display after each guess
    game_over = update_display()

    # Clear the entry field after each guess
    guess_entry.delete(0, tk.END)

# Create an input field for the guess
guess_entry = tk.Entry(root, font=("Courier", 14))
guess_entry.pack(pady=10)

# Create a button to submit the guess
guess_button = tk.Button(root, text="Guess", font=("Courier", 14), command=guess_letter)
guess_button.pack(pady=10)

# Create a button to start a new game
new_game_button = tk.Button(root, text="New Game", font=("Courier", 14), command=new_game)
new_game_button.pack(pady=10)

# Start the main loop
root.mainloop()

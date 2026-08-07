from ascii_art import STAGES
import random
import os


WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """
    Return a randomly selected word from the WORDS list
    """
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Display the current snowman ASCII art and the partially guessed word.
    """
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    print("\n")


def play_game():
    """
    Run a full round of the Snowman Meltdown game.

    This function handles:
        - Initializing game state (secret word, guessed letters, mistake counter).
        - Repeatedly prompting the user for guesses.
        - Validating input (single alphabetical character).
        - Tracking correct and incorrect guesses.
        - Updating the snowman ASCII art based on mistakes.
        - Detecting win and loss conditions.
        - Displaying the final game result.

    The game continues until:
        - The player guesses all letters correctly, OR
        - The number of mistakes reaches the maximum allowed.
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    MAX_MISTAKES = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < MAX_MISTAKES:
        os.system("cls" if os.name == "nt" else "clear")
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        # Skip invalid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        # Skip repeated guesses
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        # Add guess
        guessed_letters.append(guess)

        # Correct guess?
        if guess in secret_word:
            print("Correct!\n")
        else:
            mistakes += 1
            print("Wrong! Snowman is melting...\n")

        # Win condition
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You saved the snowman!")
            return

    # Lose condition
    display_game_state(mistakes, secret_word, guessed_letters)
    print("The snowman melted! The word was:", secret_word)

import random

# Snowman ASCII Art stages
STAGES = [
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
    """,
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
    """,
    """
      ___  
     /___\\ 
     (o o) 
    """,
    """
      ___  
     /___\\ 
    """
]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display ASCII art for current mistake count
    print(STAGES[mistakes])

    # Build display version of the secret word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    # Step 2: Show initial game state
    display_game_state(mistakes, secret_word, guessed_letters)

    # Prompt user for one guess (logic comes later)
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()

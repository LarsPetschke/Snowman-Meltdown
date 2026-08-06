import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def print_snowman(lst, mistakes):
    remaining = lst[:len(lst) - mistakes]
    for line in remaining:
        print(line)


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    MAX_MISTAKES = 5

    lst = [
        "    ___    ",
        "   /___\   ",
        "   (o o)   ",
        "   ( : )   ",
        "   ( : )   "
    ]

    while mistakes < MAX_MISTAKES:
        print_snowman(lst, mistakes)
        print("Word:  _ _ _ _ _ _ ")

        guess = input("Guess a letter: ").lower()

        if guess not in secret_word:
            mistakes += 1
            print("Wrong! Snowman is melting...")
        else:
            print("Correct!")

    print("Game over! The word was:", secret_word)


if __name__ == "__main__":
    play_game()
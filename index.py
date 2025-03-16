import random

def hangman():
    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    # List of words
    word_list = ['python', 'programming', 'hangman', 'developer', 'openai']
    chosen_word = random.choice(word_list)
    guessed_word = ['_'] * len(chosen_word)  # Display blanks for the word
    attempts = 6  # Maximum wrong guesses allowed
    guessed_letters = set()

    while attempts > 0:
        print("\nWord: " + " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            print(f"Good job! '{guess}' is in the word.")
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

        if '_' not in guessed_word:
            print("\nCongratulations! You guessed the word:", chosen_word)
            break
    else:
        print("\nGame over! The word was:", chosen_word)

# Run the game
hangman()
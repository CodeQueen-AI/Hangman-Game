# 📝 Hangman Game 
> A word-guessing game where the player has to guess a hidden word one letter at a time before running out of attempts

## ⚙️ How It Works
# 1️⃣ Word Selection

The program randomly selects a word from a predefined list

The word is displayed as underscores (_ _ _ _ ) to represent unguessed letters

# 2️⃣ User Guessing

The player guesses one letter at a time

If the letter is correct, it replaces the corresponding underscore

If incorrect, the number of attempts decreases

# 3️⃣ Game Rules

The player has 6 attempts to guess the word

The guessed letters are stored to avoid duplicate inputs

If the word is guessed correctly, the player wins

If attempts reach 0, the player loses and the correct word is revealed

# 🔧 Key Features & Functions Used

🔹 random.choice(word_list) → Randomly selects a word

🔹 enumerate(chosen_word) → Helps replace correct letters in the guessed word

🔹 set() → Stores guessed letters to prevent duplicate guesses

## *Code Queen always writes interactive and fun programs like this! 🚀🔥*









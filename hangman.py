import random

def hangman():
    # List of possible words
    word_list = ["python", "hangman", "developer", "programming", "openai", "challenge"]
    word_to_guess = random.choice(word_list).lower()
    guessed_word = ["_"] * len(word_to_guess)
    attempts_left = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Try to guess the word before you run out of attempts.")
    print("Word to guess: " + " ".join(guessed_word))
    
    while attempts_left > 0 and "_" in guessed_word:
        print("\nAttempts left:", attempts_left)
        print("Guessed letters:", ", ".join(guessed_letters))
        guess = input("Enter a letter or guess the word: ").lower()

        if len(guess) == 1:  # Single letter input
            if guess in guessed_letters:
                print(f"You've already guessed the letter '{guess}'. Try again.")
            elif guess in word_to_guess:
                print(f"Good job! The letter '{guess}' is in the word.")
                for i, letter in enumerate(word_to_guess):
                    if letter == guess:
                        guessed_word[i] = guess
            else:
                print(f"The letter '{guess}' is not in the word.")
                attempts_left -= 1
            guessed_letters.append(guess)
        elif len(guess) == len(word_to_guess):  # Full word guess
            if guess == word_to_guess:
                guessed_word = list(word_to_guess)
                break
            else:
                print("Incorrect word guess!")
                attempts_left -= 1
        else:
            print("Invalid input. Please guess a single letter or the entire word.")

        print("Current word:", " ".join(guessed_word))
    
    if "_" not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word_to_guess)
    else:
        print("\nGame over! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()

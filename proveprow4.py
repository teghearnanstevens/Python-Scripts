def main():
    secret_word = "mosiah"
    attempts = 12 
    guesses = 0
    revealed_letters = set()

    print("Welcome to the word guessing game! Guess the word with the same length as the secret word.")
    print("The secret word", "_" * len(secret_word))

    while attempts > 0:
        guess = input("What is your guess? ").strip().lower()

        if len(guess) != len(secret_word):
            print(f"Please enter a word with {len(secret_word)} letters.")
            continue

        guesses += 1

        if guess == secret_word:
            print("Congratulations! You guessed it!")
            score = attempts * 10  
            print("Your score is:", score)
            return
        else:
            attempts -= 1  

        correct_letters = set()

        for idx, letter in enumerate(guess):
            if letter == secret_word[idx]:
                correct_letters.add((letter, idx))
            elif letter in secret_word:
                correct_letters.add((letter, None))

        revealed_word = ""
        for idx, letter in enumerate(secret_word):
            if (letter, idx) in correct_letters:
                revealed_word += letter.upper()
            else:
                revealed_word += "_"

        print("Revealed word:", revealed_word)

        if revealed_word == secret_word.upper():
            print("Congratulations! You guessed it!")
            score = attempts * 10  
            print("Your score is:", score)
            break

        for letter, position in correct_letters:
            if position is None:
                print(f"Hint: The letter '{letter}' is in the word, but not in the right position.")

    else:
        print("Sorry, you've run out of attempts! The secret word was:", secret_word)

if __name__ == "__main__":
    main()
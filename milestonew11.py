def main():
    secret_word = "mosiah"
    guesses = 0

    print("Welcome to the word guessing game!")

    while True:
        guess = input("What is your guess? ").strip().lower()
        guesses += 1

        if guess == secret_word:
            print("Congratulations! You guessed it!")
            print("It took you", guesses, "guesses.")
            break
        else:
            print("Your guess was not correct.")

if __name__ == "__main__":
    main()
import random

def main():
    
    word_list = ["nephi", "shiz", "laman", "lehi", "ammon", "antinephilehi", "moroni", "jesus", "alma", "corianton", "nephites", "gadianton", "kingnoah" ]
    secret_word = random.choice(word_list)
    word_length = len(secret_word)
    
    attempts = 10 
    guesses = 0
    revealed_letters = set()

    print("Welcome to the Book of Mormon Hangman game!")
    print("The secret word is", "_" * word_length)
    print("Hint: Names in the Book of Mormon")

    while attempts > 0:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in revealed_letters:
            print("You've already guessed this letter.")
            continue

        guesses += 1

        if guess in secret_word:
            revealed_letters.add(guess)
            revealed_word = ""
            for letter in secret_word:
                if letter in revealed_letters:
                    revealed_word += letter
                else:
                    revealed_word += "_"
            print("Revealed word:", revealed_word)

            if revealed_word == secret_word:
                print("Congratulations! You guessed the word:", secret_word)
                print("Your score is:", attempts * 10)
                return
        else:
            attempts -= 1
            print("Incorrect guess. Attempts left:", attempts)

    else:
        print("Sorry, you've run out of attempts! The secret word was:", secret_word)

if __name__ == "__main__":
    main()

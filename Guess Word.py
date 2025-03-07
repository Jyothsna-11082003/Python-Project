import random
import re

# Function to read words from a file
def read_words():
    try:
        with open('words.txt', 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print('Error: words.txt file not found. Please create the file and add words.')
        return []

# Function to display the current progress of the word
def display_word(secret_word, guessed_letters):
    word_to_display = ''
    for letter in secret_word:
        if letter in guessed_letters:
            word_to_display += letter + ' '
        else:
            word_to_display += '_ '
    print("\nCurrent word:", word_to_display.strip())

# Function to get a valid letter from the user
def get_guess(guessed_letters):
    while True:
        guess = input('Enter a letter: ').lower()
        if len(guess) != 1:
            print('Error: Enter only one letter.')
        elif not re.match('[a-z]', guess):
            print('Error: Enter only letters from a to z.')
        elif guess in guessed_letters:
            print('Error: You already guessed that letter.')
        else:
            return guess

# Function to check if the word is completely guessed
def is_word_guessed(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)

# Main function to run the game
def main():
    words = read_words()
    if not words:
        print('No words found. Exiting game.')
        return

    secret_word = random.choice(words).lower()  # Randomly select a word
    attempts = 6  # Number of wrong attempts allowed
    guessed_letters = []

    print("\nWelcome to the Word Guessing Game!")
    print("You have 6 attempts to guess the word.")

    while attempts > 0:
        display_word(secret_word, guessed_letters)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print('Good guess!')
            if is_word_guessed(secret_word, guessed_letters):
                print(f'Congratulations! You guessed the word: {secret_word}')
                break
        else:
            attempts -= 1
            print(f'Wrong guess! Attempts left: {attempts}')
            if attempts == 0:
                print(f'Game over! The word was: {secret_word}')

# Run the game when the script is executed
if __name__ == '__main__':
    main()

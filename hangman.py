import random
from words import words_list
from hangman_stages import stages
import string

def getvalidwords(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = getvalidwords(words_list)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left.")
        print("Used letters:", ', '.join(used_letters))

        word_display = [letter if letter in used_letters else '-' for letter in word]
        print(stages[lives])
        print("Current word:", ' '.join(word_display))

        user_input = input("Guess a letter: ").upper()

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives -= 1
                print(f"'{user_input}' is not in the word.")
        elif user_input in used_letters:
            print("You have already used that letter. Try again.")
        else:
            print("Invalid character. Try again.")

    if lives == 0:
        print(stages[lives])
        print("You died! Sorry, the word was:", word)
    else:
        print(" Yay! You guessed the word:", word)

if __name__ == "__main__":
    hangman()

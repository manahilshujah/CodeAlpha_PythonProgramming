print("Welcome to Hangman")
import random

words= ["python", "apple", "banana", "mango", "orange"]
word = random.choice(words)
guessed = []
tries = 6

while tries > 0:
    display = ''.join([ch if ch in guessed else '_' for ch in word])
    print("Word:", display)

    if '_' not in display:
        print("You won! The word was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess not in guessed:
        guessed.append(guess)
        if guess not in word:
            tries -= 1
            print("Wrong! Tries left: ",tries)

if tries == 0:
    print("Game over! The word was:",word)


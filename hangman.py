#!/usr/bin/env python3
"""Hangman - guess the hidden word, one letter at a time. You have 6 wrong guesses."""
import argparse, random
WORDS = ["python", "github", "computer", "hangman", "keyboard", "program", "developer", "terminal"]

def play(word, guesses=None):
    guessed, wrong, max_wrong = set(), 0, 6
    guess_iter = iter(guesses) if guesses is not None else None
    while wrong < max_wrong:
        display = " ".join(c if c in guessed else "_" for c in word)
        print(f"Word: {display} | Wrong guesses left: {max_wrong - wrong}")
        if all(c in guessed for c in word):
            print(f"You win! The word was '{word}'."); return True
        letter = next(guess_iter) if guess_iter is not None else input("Guess a letter: ").strip().lower()
        if not letter: continue
        letter = letter[0]
        if letter in guessed: print("You already guessed that letter."); continue
        guessed.add(letter)
        if letter in word: print("Good guess!")
        else: wrong += 1; print("Wrong guess!")
    print(f"Game over! The word was '{word}'."); return False

def main():
    p = argparse.ArgumentParser(description="Hangman Game")
    p.add_argument("--word", help="Fix the secret word (for testing)")
    args = p.parse_args()
    play(args.word or random.choice(WORDS))

if __name__ == "__main__":
    main()

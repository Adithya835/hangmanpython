#hangman game

import random

def movie():
    movie = ["ARM","EVERST","FIRST MAN","GRAVITY","BEAST","MEN","JOKER"]
    return random.choice(movie)

def play():
    chance = 8
    word = movie()
    letter = []
    word_length = len(word)
    print(f"the selected word{word_length}letters ")
    while chance > 0:
        current = ''.join([letter if letter in letter else '_' for letter in word])
        print("current word", current)

        if current == word:
            print(" you won")
            return
        guess = input("enter ypur guess, one letter: ").lower()
        try:   
            if len(guess)!=1:
                print("please enter a single letter.")
                continue
            if not guess.isnumeric == True:
                print("please enter alphabets only.")
                continue
            if guess in letter:
                print("you've already guessed that letter.")
                continue
            letter.append(guess)
            if guess not in word:
                chance -= 1
                print(f"incorrect guess! you have{chance}chance left")
            else:
                print("good guess")
        except ValueError as e:
            print(e)
    print(f"you lost he worg'{word}'.")
play()

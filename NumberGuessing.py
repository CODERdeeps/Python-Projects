#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random as rand

print(logo)
print("Hello Take a guess between 1 and 100")


def play():
    r = rand.randint(1, 100)
    e = 10
    m = 5
    h = 1

    p = input("Choose easy, medium or hard?")

    if p == "easy":
        l = e
    if p == "med":
        l = m
    elif p == "hard":
        l = h

    while l != 0:
        g = int(input("Enter a Number between 1 and 100 :- "))
        if g == r:
            print("You Won!!")
        elif g < r:
            print("Too Low")
        else:
            print("Too High")
        l -= 1
    print("Game Over")


play()

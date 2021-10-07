"""
Write a program that asks the user to guess a random number between 1 and 10. If they guess
right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. Give
the user five numbers to guess and print their score after all the guessing is done.
"""
from random import randint
point = 0
number = randint(1, 10)
for chance in range(1, 6):
    guess = int(input("enter your guess: "))
    if guess == number:
        point += 10

    else:
        point -= 1

print(f"score: {point}")

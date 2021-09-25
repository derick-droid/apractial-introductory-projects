# Generate a random number between 1 and 10. Ask the user to guess the number and print a
# message based on whether they get it right or not.

from random import *
number = randint(1, 10)
guess = int(input("make guess: "))
if guess == number:
    print("you won")
else:
    print("you lose")
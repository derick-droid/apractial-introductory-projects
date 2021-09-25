# a simple guessing game
from random import randint
number = randint(1, 10)
guess = int(input("Enter your guess: "))
if guess > 10:
    print("higher guess")
elif guess < 1:
    print("lower guess")
elif guess == number:
    print("you have won")
else:
    print("that is wrong the answer is ", number)

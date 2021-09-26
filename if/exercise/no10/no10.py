# Write a multiplication game program for kids. The program should give the player ten ran-
# domly generated multiplication questions to do. After each, the program should tell them
# whether they got it right or wrong and what the correct answer is.
from random import *


for question in range(1, 10):
    number = randint(1, 10)  # generating the first random number
    number1 = randint(1, 10)  # generating the first random number
    multiplication = int(input(f" question {question}   {number} x {number1}: "))
    product = number * number1

    if multiplication == product:
        print("right")
    else:
        print("wrong")





# 1. Write a program that generates and prints 50 random integers, each between 3 and 6.

from random import randint
for x in range(1, 51):
    print(randint(3, 6))
"""
In the last chapter there was an exercise that asked you to create a multiplication game for
kids. Improve your program from that exercise to keep track of the number of right and
wrong answers. At the end of the program, print a message that varies depending on how
many questions the player got right.
"""
from random import randint
right_answers = 0
wrong_answers = 0
for question in range(1, 10):
    number = randint(1, 10)  # generating the first random number
    number1 = randint(1, 10)  # generating the first random number
    multiplication = int(input(f" question {question}   {number} x {number1}: "))
    product = number * number1

    if multiplication == product:
        right_answers += 1
        print("right")
    else:
        wrong_answers += 1
        print("wrong")
print(f"you got {wrong_answers} wrong ")
print(f"you got {right_answers} right ")


"""
Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it
"""


def lines(word):
    for i in range(1, 101):
        print(i + 1, word)

    return  True

lines("derrick")
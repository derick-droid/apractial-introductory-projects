"""
. Write a program that asks the user for their name and how many times to print it. The program should print out
the user’s name the specified number of times.
"""


def namesize():
    name =  input("enter name: ")
    times = int(input("number to appear: "))

    for y in range(times):
        print(name)
    return True

namesize()


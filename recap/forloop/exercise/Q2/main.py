"""
Write a program to fill the screen horizontally and vertically with your name. [Hint: add the
option end='' into the print function to fill the screen horizontally.]
"""


def horizontal():
    name = input("enter your name: ")
    if "" or "-" in name:
        print("please put valid name")
    else:
        for i in range(101):

            print(name, end=" ")
            print(name)


horizontal()


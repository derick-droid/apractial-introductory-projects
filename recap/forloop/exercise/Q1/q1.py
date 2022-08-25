"""
Write a program that prints your name 100 times
"""


def name_letter():
    name = input("enter your name: ")
    # verify the name validity
    if "" or "-" in name:
        print("please put valid name")
    else:
        for i in range(101):
            print(name)


name_letter()

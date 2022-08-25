"""
recap for loop
"""


def loop():
    # Example 1
    # The following program will print Hello ten times:
    for i in range(10):
        print("Hello")
    # Example 2
    # The program below asks the user for a number and prints its square, then asks for
    # another number and prints its square, etc. It does this three times and then prints that the loop is
    # done.

    for i in range(3):
        number = eval(input("enter number: "))
        print("The square is :", number * number)
    print("Thr loop is done")
    #
    # Example  3
    # The program below will print A, then B, then it will alternat C’s and D’ five times and then finish with the letter E once.

    print("A")
    print("B")
    for i in range (5):
        print("C")
        print("D")
    print("E")

    # Example 4
    # If we wanted the above program to print five C’s followed by five D’s, instead of
    # alternating C’s and D’s, we could do the following:
    print("A")
    print("B")
    for i in range(5):
        print("C")
    for x in range(5):
        print("D")
    print("E")

    #  example program that counts down from 5 and then prints a message
    for i in range(5, 2, -1):
        print(i)
    # trickier example
    for i in range(6):
        print("*" * i)
    for i in range(6):
        print("*" * 5)
    return True


loop()

"""
The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
number thereafter is the sum of the two preceding numbers. Write a program that asks the
user how many Fibonacci numbers to print and then prints that many.

"""


def fib():
    times = int(input("enter number of times: "))

    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, times):
        c = a + b
        a = b
        b = c
        print(c)


fib()

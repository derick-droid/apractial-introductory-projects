# 1. Write a program that prints your name 100 times.

for i in range(101):
    print("derrick okinda")

# 2. Write a program to fill the screen horizontally and vertically with your name. [Hint: add the
# option end= '' into the print function to fill the screen horizontally.]

for i in range(101):
    print("derrick okinda")
    print("derrick okinda", end="")

# 3. Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it. The
# output should look like the output below.
# 1 Your name
# 2 Your name
# 3 Your name
# 4 Your name
# ...
# 100 Your name


for i in range(101):
    print(i+1,"derrick okinda")

    # Write
    # a
    # program
    # that
    # prints
    # out
    # a
    # list
    # of
    # the
    # integers
    # from
    #
    # 1
    # to
    # 20 and their
    # squares.The
    # output
    # should
    # look
    # like
    # this:
    # 1 - -- 1
    # 2 - -- 4
    # 3 - -- 9
    # ...
    # 20 - -- 400

for i in range(21):
    print(i*i,i)

# 5. Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89.

for i in range(8,90,3):
    print(i)

# 6. Write a program that uses a for loop to print the numbers 100, 98, 96, . . . , 4, 2.

for i in range(100, 2, -2):
    print(i)
# Write a program that uses exactly four for loops to print the sequence of letters below.
# AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG

for i in range(11):
    print("A")
for i in range(7):
    print("B")
print("C")
print("D")
print("C")
print("D")
print("C")
print("E")
for i in range(6):
    print("F")
print("G")

# 8. Write a program that asks the user for their name and how many times to print it. The pro-
# gram should print out the user’s name the specified number of times.

name = input("enter name: ")
times = int(input("how many times:  "))

for i in range(times):
    print(name)
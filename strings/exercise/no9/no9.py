"""
Ask the user for a number and then print the following, where the pattern ends at the number
that the user enters.
1
 2
  3
   4
"""
number = int(input("enter number: "))
for num in range(1, number + 1):
    for num1 in range(1, number-num - 1):
        print(end="")
    for num1 in range(1, num + 1):
        print(num, end=" ")
    print()

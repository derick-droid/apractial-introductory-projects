"""
Write a program to compute the sum 1 − 2 + 3 − 4 + · · · + 1999 − 2000 .
"""
sum = 0
for number in range(1, 2001):
    sum = number + sum

print(sum)


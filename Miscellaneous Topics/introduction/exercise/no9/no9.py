"""
Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect
cubes, or perfect fifth powers.

"""
from math import sqrt
count = 0
count_1 = 0
count_2 = 0
for num in range(1, 1001):
    if sqrt(num) % 1 != 0:
        count += 1
    if (num ** 1/3) % 1 != 0:
        count_1 += 1
    if (num ** 1/5) % 1 != 0:
        count_2 += 1
print(f"there are {count} non perfect squares")
print(f"there are {count_1} non perfect cubes")
print(f"there are {count_2} non perfect fifth powers")
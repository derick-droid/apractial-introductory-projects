"""
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
1.
"""
count = 0
for number in range(1, 101):
    square_number = (number ** 2) % 10
    if square_number == 1:
        count += 1

print(f"there are {count} numbers ")


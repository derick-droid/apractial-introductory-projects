"""
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
4 and how many end in a 9.
"""
count = 0
count2 = 0
for number in range(1, 101):
    square_number = (number ** 2) % 10
    square_number1 = (number ** 2) % 10
    if square_number == 4:
        count += 1
    elif square_number1 == 9:
        count2 += 1

print(f"ending with 9 are {count2}")
print(f"ending with 4 are {count}")
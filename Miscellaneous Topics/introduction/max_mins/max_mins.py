"""
A common programming task is to find the largest or smallest value in a series of values
"""
largest_number = int(input("enter the initial number: "))
for numbers in range(10):
    new_number = int(input("enter new number: "))
    if new_number > largest_number:
        largest_number = new_number

print(f" the largest number is {largest_number}")

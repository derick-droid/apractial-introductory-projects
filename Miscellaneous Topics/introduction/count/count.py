# basics in counting
"""
This program gets 10 numbers from the user and counts how many of those numbers
are greater than 10.
"""""

count = 0
for number in range (10):
    num = int(input("enter number: "))
    if num > 10:
        count += 1

print(f"there are {count} greater numbers  than 10")

print()


"""
This modification of the previous example counts how many of the numbers the user
enters are greater than 10 and also how many are less than  10. To count two things we use two count
variables.
"""

count = 0
count2 = 0
for number in range(10):
    num = int(input("enter number: "))
    if num > 10:
        count += 1
    elif num < 10:
        count2 += 1

print(f"there are {count} number greater than 10")
print(f"there are {count2} numbers less than 10")

print()
"""
This program counts how many of the
squares from 1 to 100  end in a 4.
"""
count = 0
for number in range(1, 101):
    if (number ** 2) % 10 == 4:
        count += 1

print(f"there are {count} which ends in 4 ")

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

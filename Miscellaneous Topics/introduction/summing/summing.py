"""
This program will add up the numbers from 1 to 100. The way this works is that each
time we encounter a new number, we add it to our running total, s .
"""
sum = 0
for number in range(1, 101):
    sum = number + sum

print(f"the sum is {sum}")


"""
This program that will ask the user for 10 numbers and then computes their average.
"""
sum = 0

for number in range(10):
    num = int(input("enter number: "))
    sum = num + number
    average = sum/10

print(f"the average of numbers you have entered is {average}")

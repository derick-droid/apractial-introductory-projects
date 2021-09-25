# Write a program that asks the user to enter a number and prints out all the divisors of that
# number.

num = int(input("enter number: "))
for number in range(1, num+1):
    if num % number == 0:
        print(number)
        
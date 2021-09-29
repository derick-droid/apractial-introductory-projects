"""
Write a program that asks the user to enter a number and prints the sum of the divisors of
that number. The sum of the divisors of a number is an important function in number theory.
"""
sum = 0
num = int(input("enter a number: "))
for number in range(1, num+1):
    if num % number == 0:
        sum = number + sum

print(f"the sum of the divisors are {sum}")
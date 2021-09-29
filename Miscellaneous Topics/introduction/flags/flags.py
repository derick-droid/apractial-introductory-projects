"""
A flag variable can be used to let one part of your program know when something happens in
another part of the program. Here is an example that determines if a number is prime
"""
flag = 0
num = int(input("enter number: "))
for number in range(1, num):
    if num % number == 0:
        flag = 1

if flag == 1:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")


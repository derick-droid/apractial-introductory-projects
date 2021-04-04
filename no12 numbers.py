# Write a program that asks the user for a number and prints out the factorial of that number.
num = int(input("enter number: "))

# check if number is less than zero
if num < 0:
    print("this number has no factorial value")
# check if number is zero
if num == 0:
    print("the factorial number is 1")

factorial = 1
for i in  range(1, num +1):
    factorial = factorial * i
print(f"the factorial of the number is {factorial}")
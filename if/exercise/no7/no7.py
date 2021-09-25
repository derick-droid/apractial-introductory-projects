# Write a program that asks the user for two numbers and prints Close if the numbers are
# within .001 of each other and Not close otherwise.

number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))
differnce = abs(number2 - number1)
if differnce == 0.001:
    print("close")
else:
    print("not close")
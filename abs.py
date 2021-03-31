# Write a program that asks the user to enter two numbers, x and y , and computes
# |x− y|
# x+ y .

num1 = int(input("enter: "))
num2 = int(input("enter: "))
abss = abs(num1 - num2)
add = num1 + num2
print(abss / add)
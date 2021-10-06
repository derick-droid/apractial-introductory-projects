"""
Write a program that swaps the values of three variables x , y , and z , so that x gets the value
of y , y gets the value of z , and z gets the value of x .
"""

x = 10
y = 34
z = 90
# swapping the variable
hold_x = x
hold_y = y
hold_z = z

x = hold_y
y = hold_z
z = hold_x
print(x)
print(y)
print(z)

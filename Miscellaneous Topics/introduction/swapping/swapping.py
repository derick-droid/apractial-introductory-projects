"""
Quite often we will want to swap the values of two variables, x and y . It would be tempting to try
the following:
"""
x = 15
y = 12
hold = y
y = x
x = hold
print(y)
print(x)

"""
In many programming languages, this is the usual way to swap variables. Python, however, pro-
vides a nice shortcut:
"""
x, y = x, y
print(x)
print(y)


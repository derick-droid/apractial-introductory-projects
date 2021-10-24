"""
People often forget closing parentheses when entering formulas. Write a program that asks
the user to enter a formula and prints out whether the formula has the same number
of opening and closing parentheses

"""

user_formula = input("enter a formula: ")
if "()" in user_formula:

    print("ok")
else:
    print("forgotten parenthesis")

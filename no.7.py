# Write a program that asks the user to enter an angle between −180 ◦ and 180 ◦ . Using an
# expression with the modulo operator, convert the angle to its equivalent between 0 ◦ and
# 360 ◦ .

angle = float(input("enter angle: "))
if angle > 180:
    print("invalid entry! please try again")
else:
    print(angle % 360)
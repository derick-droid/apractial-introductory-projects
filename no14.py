# Write a program that asks the user to enter an angle in degrees and prints out the sine of that
# angle.

import math
num = int(input("enter angle: "))
deg = math.radians(num)
sine = math.sin(deg)
print(sine)

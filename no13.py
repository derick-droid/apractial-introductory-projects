# . Write a program that asks the user for a number and then prints out the sine, cosine, and
# tangent of that number.
from math import sin, cos, tan
num = int(input("enter number: "))
sine = sin(num)
cosine = cos(num)
tangent = tan(num)

print(sine)
print(cosine)
print(tangent)
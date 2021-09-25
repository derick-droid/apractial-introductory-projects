# A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
# unless they are also divisible by 400. Write a program that asks the user for a year and prints
# out whether it is a leap year or not.

year = int(input("enter a year: "))
if year % 400 == 0:
    print(" leap year ")
elif year % 100 != 0 and year % 4 == 0:
    print(" not leap year")
else:
    print("not leap year")

print("it is done ")


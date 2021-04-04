#(a)
# One way to find out the last digit of a number is to mod the number by 10. Write a
# program that asks the user to enter a power. Then find the last digit of 2 raised to that
# power.

power = int(input("enter power: "))
result = 2 ** power
final = result % 10
print(f"The last digit is {final}")
#(b)

# One way to find out the last two digits of a number is to mod the number by 100. Write
# a program that asks the user to enter a power. Then find the last two digits of 2 raised to
# that power.

power1 = int(input("enter power1: "))
result1 = 2 ** power1
final1 = result1 % 100
print(f"the las two dgts are: {final1}")

# (c)
# Write a program that asks the user to enter a power and how many digits they want.
# Find the last that many digits of 2 raised to the power the user entered.
power2  = int(input("enter power2: "))
dgtz = int(input("enter digits wanted: "))
result2 = 2 ** power2
digits = round(result2, dgtz)
final2 = digits % 10
print(f"the last digit is {final2}")


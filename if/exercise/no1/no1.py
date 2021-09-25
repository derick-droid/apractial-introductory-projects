# Write a program that asks the user to enter a length in centimeters. If the user enters a negative
# length, the program should tell the user that the entry is invalid. Otherwise, the program
# should convert the length to inches and print out the result. There are 2.54 centimeters in an
# inch.

length = float(input("enter length in cm : "))
if length < 0:
    print("invalid length")
else:
    new_length = length / 2.54
    print(new_length)



# Write a program that asks the user to enter a year and prints out the date of Easter in that
# year
import math
century = 19
Year = int(input("enter year: "))  # year
# checking if year given is four figures
if Year < 1000:
    print("invalid year")
# the Algorithm
ch = math.floor(Year % 9)
m = math.floor((15 + century - (ch / 4) - ((8*ch + 13)/25)) % 30)
n = math.floor((4 + century - (ch/4)) % 7)
a = math.floor(Year % 4)
b = math.floor(Year % 7)
d = math.floor((19*ch + m) % 30)
e = math.floor((2*a + 4*b + 6*d + n) % 7)
day = math.floor(22 + d + e)
# A = Y % 19
# B = Y % 4
# C = Y % 7
#
# P = math.floor(Y / 100)
# Q = math.floor((13 + 8 * P) / 25)
# M = (15 - Q + P - P // 4) % 30
# N = (4 + P - P // 4) % 7
# D = (19 * A + M) % 30
# E = (2 * B + 4 * C + 6 * D + N) % 7
# days = (22 + D + E)

if d == 29 and e == 6:
    print(Year, " 19th April ")
elif d == 28 and e == 6 and m == 2 == 5 == 10 == 13 == 16 == 21 == 24 == 39:
    print(Year, " 18th April ")
else:
    if day > 31:
        print(f"Easter is {Year} {day - 31} march")

    else:
        print(f"{Year}, March, {day}")

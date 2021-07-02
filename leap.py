# A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
# unless they are also divisible by 400. Ask the user to enter a year, and,
# determine how many leap years there have been between 1600 and that year.

year = int(input("enter year : "))
list_year = []
for years in range(1600, year + 1):

    if years % 4 == 0 and years % 100 != 0:

        list_year.append(years)
    elif years % 400 == 0:
        list_year.append(years)
print(len(list_year))

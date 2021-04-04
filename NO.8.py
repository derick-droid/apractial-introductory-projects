# Write a program that asks the user for a number of seconds and prints out how many minutes
# and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
# operator to get minutes and the % operator to get seconds.]

num = int(input("enter: "))
minutes = num // 60
seconds = num % 60
print(f"{num} seconds is {minutes} minutes and {seconds} seconds")
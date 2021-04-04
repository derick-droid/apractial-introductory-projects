# Write a program that asks the user to enter a weight in kilograms. The program should
# convert it to pounds, printing the answer rounded to the nearest tenth of a pound.

weight = int(input("enter weight in kilograms: "))
if weight > 350:
    print("invalid weight ")
else:
    result = weight * 2.2
    add = round(result, 10)
    print(f"weight in pound is {add}")

# Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm ,
# and asks them how many hours into the future they want to go. Print out what the hour will
# be that many hours into the future, printing am or pm as appropriate

user_hour = int(input("enter the hour: "))
if user_hour > 12:
    print("enter between 1 and 12 ")
else:
    period_time = int(input("AM(1) OR PM(2): "))
    hour_long = int(input("how many hours long: "))

    new_hour = user_hour + hour_long
    if period_time == 1 and new_hour < 12:
        print(f"{new_hour} am")
    else:
        print(f"{new_hour} pm")









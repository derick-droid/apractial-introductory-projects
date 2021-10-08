"""
This exercise is about the well-known Monty Hall problem. In the problem, you are a contestant on a game show. The host, Monty Hall, shows you three doors. Behind one of those
doors is a prize, and behind the other two doors are goats. You pick a door. Monty Hall, who
knows behind which door the prize lies, then opens up one of the doors that doesn’t contain
the prize. There are now two doors left, and Monty gives you the opportunity to change your
choice. Should you keep the same door, change doors, or does it not matter?

(a) Write a program that simulates playing this game 10000 times and calculates what percentage of the time you would win if you switch and what percentage of the time you
would win by not switching.

(b) Try the above but with four doors instead of three. There is still only one prize, and
Monty still opens up one door and then gives you the opportunity to switch.

"""

play_times = 10  # playing number of times
point_switch = 0  # for tracking the percentage win if you switch the door
point_not_switch = 0  # for tracking the percentage win if you do not switch the door

# the doors available with their prices for the game

door_1 = "goat"
door_2 = "car"
door_3 = "goat"


for chance in range(1, play_times + 1):
    choose = input("choose door: ").lower()

    # if door 2 is chosen
    if choose == "door 2":
        print("congratulation you won a car")

# if door 2 is chosen
    elif choose == "door 1":
        switch = input("door 3 is a goat would you like to switch: ")
        if switch.lower() == "yes":
            choose = input("choose the remaining door: ")
            if choose == "door 3":
                print("the door is already opened")
            elif choose == "door 2":
                print("congratulation you won a car")
                point_switch += 1
        elif switch.lower() == "no":
            print("you choose a goat")
            point_not_switch += 1

# if door 3 is chosen
    elif choose == "door 3":
        switch = input("door 1 has a goat would you like to switch: ")
        if switch.lower() == "yes":
            choose = input("choose the remaining door: ")
            if choose.lower() == "door 1":
                print("door is already opened")
            elif choose.lower() == "door 3":
                print("you won a goat")
                point_not_switch += 1
            elif choose.lower() == "door 2":
                print("you won a car")
                point_switch += 1
        elif switch.lower() == "no":
            print("you won a goat")
            point_not_switch += 1

    else:
        print("invalid choice ")

percentage_win_switch = (point_switch / play_times) * 100
percentage_win_not_switch = (point_not_switch / play_times) * 100
print(f"the percentage win if you switch is {percentage_win_switch} % ")
print(f"the percentage win if you do not switch is {percentage_win_not_switch} % ")



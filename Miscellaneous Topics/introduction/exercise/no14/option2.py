"""
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
door_4 = "goat"


for chance in range(1, play_times + 1):
    choose = input("choose door: ").lower()

    # if door 2 is chosen
    if choose == "door 2":
        print("congratulation you won a car")

# if door 1 is chosen
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
        else:
            print("invalid choice")

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
            elif choose.lower() == "door 4":
                print("you won a goat")
        elif switch.lower() == "no":
            print("you won a goat")
            point_not_switch += 1
        else:
            print("invalid choice")

            # if door 4 is chosen
    elif choose == "door 4":
        switch = input("door 1 has a goat would you like to switch: ")
        if switch.lower() == "yes":
            choose = input("choose the remaining doors: ")
            if choose == "door 1":
                print("the door is already opened")
            elif choose == "door 2":
                print("you won a car")
                point_switch += 1
            elif choose == "door 3":
                print("you won a goat")
            elif choose == "door 4":
                print("you won a goat")

        elif switch.lower() == "no":
            print("you won a goat")
            point_not_switch += 1
        else:
            print("invalid choice")
    else:
        print("invalid choice ")

percentage_win_switch = (point_switch / play_times) * 100
percentage_win_not_switch = (point_not_switch / play_times) * 100
print(f"the percentage win if you switch is {percentage_win_switch} % ")
print(f"the percentage win if you do not switch is {percentage_win_not_switch} % ")



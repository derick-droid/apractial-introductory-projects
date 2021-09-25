# A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
# items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
# program that asks the user how many items they are buying and prints the total cost.

items = int(input("how many items: "))
if items < 10:
    cost = 12 * items
    print(f"total cost ${cost}")
elif items >= 10 and items <= 99:
    cost = 10 * items
    print(f"total cost ${cost}")
elif items >= 100:
    cost = 7 * items
    print(f"total cost ${cost}")
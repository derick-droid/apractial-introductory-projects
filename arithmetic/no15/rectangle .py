# Write a program that draws “modular rectangles” like the ones below. The user specifies the
# width and height of the rectangle, and the entries start at 0 and increase typewriter fashion
# from left to right and top to bottom, but are all done mod 10. Below are examples of a 3 × 5
# rectangle and a 4 × 8 .

# for i in range(3):
#     for x in range(5):
#         print("x", end=" ")
#     print()

x = eval(input('jumlah kolom'))
y = eval(input('jumlah barisan '))
z = -1
for i in range(1, x+1):
    for j in range(1, y + 1):
        z = (z + 1) % 10
        print(z, end=' ')

    print(' ')

#4. Write a program that computes and prints the result of
#512 − 282
# It is roughly .1017.
#47 · 48 + 5

x = 512
y = 282
z = 47.48
v = 5

p = x-y
b = z+v
print(p/v)


# Ask the user to enter a number. Print out the square of the number, but use the sep optional
# argument to print it out in a full sentence that ends in a period. Sample output is shown
# below.
# Enter a number: 5
# The square of 5 is 25.

number = int(input("Enter number:   "))
print(" the square is ", number * number)

# Ask the user to enter a number x . Use the sep optional argument to print out x , 2x , 3x , 4x ,
# and 5x , each separated by three dashes, like below.
# Enter a number: 7
# 7---14---21---28---35

number1 = int(input("enter number:  "))
print(number1, "--", number1*2, "--", number1*3, "--", number1*4, "--", number1*5)

# Write a program that asks the user to enter three numbers (use three separate input state-
# ments). Create variables called total and average that hold the sum and average of the
# three numbers and print out the values of total and average .

number2 = int(input("enter number:  "))
number3 = int(input("enter number:  "))
number4 = int(input("enter number:  "))

total = number2 + number4 + number3
average = total/ 3
print(average)

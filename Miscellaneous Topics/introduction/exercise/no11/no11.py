"""
Write a program that computes the factorial of a number. The factorial, n!, of a number n is the
product of all the integers between 1 and n, including n. For instance, 5! = 1 · 2 · 3 · 4 · 5 = 120.
[Hint: Try using a multiplicative equivalent of the summing technique.]
"""
factorial = 1
number = int(input("Enter number: "))

if number < 0:
    print("negative number does not have a factorial")


else:

    for num in range(1, number + 1):
        factorial = factorial * num


print(f"the factorial number of {number} is {factorial}")
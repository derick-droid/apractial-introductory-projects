"""
Write a program that asks the user to enter a value n , and then computes (1 + 1/2 + 1/3 + · · · + 1 /n ) −
ln(n) . The ln function is log in the math module.
"""
from math import log
answer = 0
value_n = int(input("enter a value: "))
for number in range(1, value_n):
    fraction_form = (1 + 1/number + 1/value_n)
    number_log = (log(value_n))
    answer_log = fraction_form - number_log
    answer = answer_log

print(answer)



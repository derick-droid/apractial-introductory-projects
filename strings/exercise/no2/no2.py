"""
A simple way to estimate the number of words in a string is to count the number of spaces
in the string. Write a program that asks the user for a string and returns an estimate of how
many words are in the string.

"""
count = 0
word = input("enter a word: ")
for ch in word:
    if ch.isspace():

        count += 1
print(count + 1)


"""
Write a program that asks the user to enter a word and prints out whether that word contains
any vowels.
"""
word = input("enter a word: ")
if "a" in word or "e" in word or "i" in word or "o" in word or "u" in word:
    print("the word contains vowels")
else:
    print("it has no vowel")
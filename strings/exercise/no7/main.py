"""
Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forwards.

"""
word = input("enter a word: ")
backward_string = word[::-1]
if word == backward_string:
    print("palindrome word")
else:
    print("not palindrome")
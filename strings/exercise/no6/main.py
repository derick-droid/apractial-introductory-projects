"""
Write a program that asks the user to enter a string s and then converts s to lowercase,
removes all the periods and commas from s, and prints the resulting string.

"""

string = input("enter a string: ")
for items in string:
    if "," or "." in string:
        string = string.replace(",", "" and ".", "")

print(string)
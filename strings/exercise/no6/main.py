"""
Write a program that asks the user to enter a string s and then converts s to lowercase,
removes all the periods and commas from s, and prints the resulting string.

"""
string = input("enter string: ").lower()
for ch in ', .':
    string = string.replace(ch, "")

print(string)

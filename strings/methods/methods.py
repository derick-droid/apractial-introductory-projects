"""
methods associated with strings

"""
# isalpha() checks if a string is only a letter

letter = input("enter string: ")
if letter[0].isalpha():
    print("it has no number")
else:
    print("it has number")

# \n to create space
print("Hi \nthere")

# \ inserting a apostrophes
print("I can\'t go with you")

# printing 10 black line

print("\n" * 9)

"""
Write a program that asks the user for a string and prints out the location of each 'a'
in the string
"""
word = input("enter word: ")
for letter in range(len(word)):
    if word[letter] == "a":
        print(letter)

"""
Example 3 Write a program that asks the user for a string and creates a new string that doubles
each character of the original string. For instance, if the user enters Hello, the output should be
HHeelllloo.
"""

word = input("enter a word: ")
for l in word:
    print(l * 2)

"""
Write a program that asks the user to enter a string. The program should then print the
following:
(a) The total number of characters in the string
(b) The string repeated 10 times
(c) The first character of the string (remember that string indices start at 0)
(d) The first three characters of the string
(e) The last three characters of the string
(f) The string backwards
(g) The seventh character of the string if the string is long enough and a message otherwise
(h) The string with its first and last characters removed
(i) The string in all caps
(j) The string with every a replaced with an e

(k) The string with every letter replaced by a space

"""

string = input("Enter a string: ")
print(string[::-1])
print(len(string))
print(string * 10, sep=" ")
print(string[0])
print(string[:3])
print(string[-3:])

if len(string) < 7:
    print("the string is less than seven")
else:
    print(string[6:])

string.replace(string[1:], "" )
string.replace(string[-1:], "")


print(string[1:-1])
print(string.upper())
new_string = " "

# replacing "a" with "e"
for ch in string:
    if ch == "a":
        new_string = string.replace(ch, "e")
        print(new_string)

# replacing with space
another_string = ""
for item in string:
    another_string = string.replace(item, " ")
    print(another_string)
print(another_string)

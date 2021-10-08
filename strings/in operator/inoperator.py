# using the in operator to check if the string contains some elements
s = " "
print(s)
for i in range(10):
    letter = input("enter a letter: ")
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        s = s + letter

print(s)
if "a" in s:
    print("yes it is ")
else:
    print("no it is not")

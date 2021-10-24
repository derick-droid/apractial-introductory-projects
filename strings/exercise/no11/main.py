"""
Write a program that asks the user to enter a word that contains the letter a. The program
should then print the following two lines: On the first line should be the part of the string up
to and including the the first a, and on the second line should be the rest of the string. Sample
output is shown below:
Enter a word: buffalo
buffa
lo
"""
word = input("enter a word: ")
index_a = word.index("a")
print(word[:index_a + 1])
print(word[index_a + 1:])
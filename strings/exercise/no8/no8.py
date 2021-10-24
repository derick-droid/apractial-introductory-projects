"""
At a certain school, student email addresses end with @student.college.edu, while professor email addresses end with @prof.college.edu. Write a program that first asks the
user how many email addresses they will be entering, and then has the user enter those addresses. After all the email addresses are entered, the program should print out a message
indicating either that all the addresses are student addresses or that there were some professor addresses entered.
"""
flag1 = 0
flag = 0
number = int(input("how many number emails: "))
for email in range(number):
    Email = input("enter email :")
    Email_index = Email.index("@")
    if Email[Email_index:] == "@student.college.edu":
        flag = 1
    elif Email[Email_index:] == "@prof.college.edu":
        flag1 = 0
    else:
        print("invalid email")

if flag1 == 1:
    print("all the address are students")
elif flag == 1:
    print("there are some professor address ")


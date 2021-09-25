# Write a program that asks the user how many credits they have taken. If they have taken 23
# or less, print that the student is a freshman. If they have taken between 24 and 53, print that
# they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.

credits_taken = int(input("how many credits taken: "))
if credits_taken <= 23:
    print("the student is a freshman")
elif credits_taken >= 23 and credits_taken <= 53:
    print("the students is a sophomore")
elif credits_taken >= 53 and credits_taken <= 83:
    print("the student is a juniors")
elif credits_taken >= 84:
    print("the student is a seniors")

    

"""
suppose here is one question

child : 0 to 11
Teen: 12 to 17
Adult : 18 to 64
"""

age = int(input("What is Your age:"))
if (age >= 0 and age <= 11):
    print("Child")
elif (age >= 12 and age <=17):
    print("Teen")
elif (age >= 18 and age <= 64):
    print("Adult")
else:
    print("wtf")

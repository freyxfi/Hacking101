"""
You are given a list of contacts, where each contact is represented by a tuple, with the name and age of the contact. 
Complete the program to get a string as input, search for the name in the list of contacts and output the age of the contact in the format presented below: 
 
Sample Input 
John 
 
Sample Output  
John is 31
"""

contacts = [
        ('James', 42),
        ('Amy', 24),
        ('John', 31),
        ('Amanda', 63),
        ('Bob',18)
        ]
fools = dict(contacts)
name = input()
if name in fools:
    print(name + " is " + str(fools.get(name)))
else:
    print("Not Found")

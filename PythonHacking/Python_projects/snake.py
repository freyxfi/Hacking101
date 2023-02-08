import random

b = random.randint(3,20)
count = 0 
for i in range(200):
    y = random.randint(3,20)
    if y == b or count ==1 :
        print("\u2b1b"*(b-1)+"\U0001f7e8")
        count = 0
        continue
    elif y > b :
        print("\u2b1b"*(b-1)+"\U0001f7e8"*(y-b+1))
        count = 1
    else :
        print("\u2b1b"*(y-1)+"\U0001f7e8"*(b-y+1))
        count = 1
    b = y

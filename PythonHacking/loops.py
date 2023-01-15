a = 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)
print("_________________")
a = 0
while a < 5:
    a +=1
    print(a)
print("_________________")
for i in [0,1,2,3,4]:
    print(i+1)
print("_________________")
for i in range(5):
    print(i+1)
print("_________________")
for i in range(2):
    for j in range(2):
        print(i,j)
print("_________________")
for i in range(5):
    if i == 2:
        break
    print(i)
print("_________________")
for i in range(3):
    if i == 1:
        continue
    print(i)
print("_________________")
for i in range(3):
    if i == 2:
        pass
    print(i)
print("_________________")
for c in "Frey0xD":
    print(c)

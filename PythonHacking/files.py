f = open('top-100.txt')
print(f)

f = open('top-100.txt', 'rt')
print(f)

print(f.readlines())
print(f.readlines())

f.seek(0)
print(f.readlines())

f.seek(0)
for line in f:
    print(line.strip())
f.close()

f = open("test.txt", "w")
f.write("testing\n")
f.close()

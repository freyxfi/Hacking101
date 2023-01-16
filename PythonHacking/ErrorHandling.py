print(1)
print(2)

try:
    gkjsbgkjbdfkjgbgkbnsk
except:
    print("what are you trying to do ??")

try:
    f = open("dfskjgdfk")
except FileNotFoundError:
    print("The File is Not Found in Frey PC")
except Exception as c:
    print(c)
finally:
    print("No Error 404")

n = 100
if n == 0:
    raise Exception("n can't be 0")
if type(n) is not int:
    raise Exception("n must be of int type")

print(1/n)

n = 0
assert(n !=0)
print(1/n)

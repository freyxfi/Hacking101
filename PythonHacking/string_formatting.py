nums = [4,5,6]
msg = "Numbers: {0}, {2}, {1}".format(nums[0],nums[1],nums[2])
print(msg)

a = "{x}, {y}".format(x=5,y=6)
print(a)

str="{c},{b},{a}".format(a=5,b=9,c=7)
print(str)

x = ",".join(["spam","eggs","ham"])
print(x)

lambo = "That was a really badass car"
x = lambo.split(' ')
print(x)

bitch = "Hello Bitch"
x = bitch.replace("Bitch", "Beautiful")
print(x)

print("this is some random sentence".upper())
print("this is some random sentence".lower())

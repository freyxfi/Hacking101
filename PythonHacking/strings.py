string1 = "Follow @Frey0xD"
string2 = 'Follow @Frey0xD'
print(string1)
print(string2)
string3 = """I am a long 
long
string!"""
print(string3)
#############################################################
string4 = "I\"m a string"
string5 = "I\'m a string"
string6 = 'I\'m a string'
print(string4)
print(string5)
print(string6)
#############################################################
string7 = "I\"m a string\nI\"m on a new line!"
string8 = "\\ \x41\x42\x43"
print(string7)
print(string8)
string9 = "fuckyou\n"*10
print(string9)
print(len(string7))
print("fuckyou" in string9)
print(string4.startswith("I"))
print(string4.index("string"))
hack_passwd = "       This is my password!        "
print(hack_passwd)
print(hack_passwd.strip())
print(hack_passwd.replace("!","?"))
print(hack_passwd.split())
strhack = "Hack the planet"
print(strhack.encode())
print(strhack.encode("utf-8"))
print(strhack.rjust(25,"X"))


def function1():
    print("Hello there from function1")
function1()
function1()

def function2():
    return "Hello there from function 2"

return_from_the_function2 = function2()
print(return_from_the_function2)

def function3(s):
    print("\t{}".format(s))

function3("Parameter")

def function4(s1, s2):
    print("{} {}".format(s1,s2))

function4("Hello", "Yo")

function4("Any","Thing")
function4(s1="Thing", s2="Any")

def function5(s1 = "Default"):
    print("{}".format(s1))

function5()

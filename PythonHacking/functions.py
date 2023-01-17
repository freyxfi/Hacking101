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
function5("Anything")

def function6(s1, *more):
    print("{} {}".format(s1, " ".join([s for s in more])))

function6("yo yo")
function6("lol", "this", "will", "work")

def function7(**ks):
    for a in ks:
        print(a, ks[a])
        
function7(a="1", b="2", c="3")

def function8(s,f,i,l):
    print(type(s))
    print(type(f))
    print(type(i))
    print(type(l))

function8("Hello", 3.0, 3, ["L", "i", "s", "t"])

v = 100
print(v)
def function9():
    global v
    v += 1
    #v  = 50
    print(v)

function9()
print(v)

def function10():
    print("Hello from the function10")

def function11():
    function10()
    print("Hello from the function11")

function11()

def function12(x):
    print(x)
    if x > 0:
        function12(x-1)

function12(5)

def function13(x):
    while x >= 0:
        print(x)
        x -= 1

function13(5)

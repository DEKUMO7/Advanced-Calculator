import math
try:
    a = int(input("=> "))
except:
    print("enter a valid number...")
    a = int(input("=> "))

c = input("chose operator ( +  -  *  /  **  %  //  [sqrt]  [stop] )=> ")

if (c == "stop"):
    print("exit")
    quit()

elif (c == "sqrt"):
    print(math.sqrt(a))
    quit()

b = int(input("=> "))
d = 0

if (c == "/" or b == 0 ):
    print("cannot divide by zero...")
    quit()
elif (c == "+"):
    e = a + b
    print(e)
    d += e
         
elif (c == "-"):
    f = a - b
    print(f)
    d += f

elif (c == "/"):
    g = a / b
    print(g)
    d += g

elif (c == "*" ):
    h = a * b
    print(h)
    d += h

elif (c == "**"):
    i = a ** b
    print(i)
    d += i

elif (c == "%"):
    j = a % b
    print(j)
    d += j

elif (c == "//"):
    k = a // b
    print(k)
    d += k

else:
    print("invalid operator...")

while  True:
    c = input("chose operator ( +  -  *  /  **  %  //  [stop] )=> ")
    if (c == "stop"):
        print("exit")
        break

    elif (c == "sqrt"):
        print(math.sqrt(d))
        break

    try:
        b = int(input("=> "))
    except:
        print("enter a valid number...")
        b = int(input("=> "))
    
    if (c == "/" or b == 0):
        print("cannot divide by zero...")
        break

    elif (c == "+"):
        e = d + b
        d -= d
        d += e
        print(d)

    elif (c == "-"):
        f = d - b
        d -= d
        d += f
        print(d)

    elif (c == "/"):
        g = d / b
        d -= d
        d += g
        print(d)

    elif (c == "*"):
        h = d * b
        d -= d
        d += h
        print(d)

    elif (c == "**"):
        i = d ** b
        d -= d
        d += i
        print(d)

    elif (c == "%"):
        j = d % b
        d -= d
        d += j
        print(d)
    elif (c == "//"):
        k = d // b
        d -= d
        d += k
        print(d)
    else:
        print("invalid operator...")

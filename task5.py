import math
def area(x,y,z) :
    s=(x+y+z)/2
    print("Semi-perimeter: ",s)
#Herons formula
    a = (s*(s-x)*(s-y)*(s-z))**0.5
    print(" ")
    print("Area of triangle: ", a)

g=input("Side A: ")
h=input("Side B: ")
i=input("Side C: ")

x = float(g)
y = float(h)
z = float(i)

area(x,y,z)
print("")

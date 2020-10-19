def max_Num(x,y,z) :

    if (x>=z and x>=y) :
        print ("The first number is the maximum : ",x)
    elif (y>=z and y>=x) :
        print ("The second number is the maximum : ",y)
    else :
        print ("The third number is the maximum : ",z)


g=input("Insert first number : ")
h=input("Insert Second number : ")
i=input("Insert Third number : ")

x=float(g)
y=float(h)
z=float(i)

print(" ")
max_Num(x,y,z)


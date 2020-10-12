import math
def numbMinHrsConv(x) :
    y=g/60;
    z=g%60;
    h=math.floor(y);
    if g> 120 : 
        print(h," hours,", z, " minutes");
    else :
        print(h," hour,", z, " minutes");

print(" ");
x=input("Insert number of minutes : ");
g=int(x);
numbMinHrsConv(x);
print(" ");


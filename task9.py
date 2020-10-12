import math

n=1000;
h=math.ceil((n/3)-1);
w=math.ceil((n/5)-1);
g=range(h);
x=range(w);

i=0;
j=0;
z=0;
q=0;
for i in g :
    i=i+1;
    j=3*i;
    z=z+j;

print("sum z : ", z);
for u in x :
    u=u+1;
    y=5*u;
    q=q+y;

print("sum q :", q);
print(" ");
print("sum total :" , q+z);
print(" ");


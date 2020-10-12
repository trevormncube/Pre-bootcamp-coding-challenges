def celsToFahr(x) :
    z=x/5*9+32;
    print( "You have entered ", x , "degrees celsius, that is equal to ", z, "degrees farhenheit");

def fahrToCels(y) :
    h=(y-32)*5/9;
    print( "You have entered ", y , "degrees fahrenheit, that is equal to ", h, "degrees celsius");

print(" ");
g=input("insert temperature in celsius:  ");
r=input("insert temperature in Fahrenheit:  ");


x = float(g);
y = float(r);

print(" ");
celsToFahr(x);
fahrToCels(y);

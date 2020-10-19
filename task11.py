def common(x,y):
    if(len(x)<len(y)):
        for j in f:
            if x[j] in y:
                print(x[j])
                j=j+1
            else:  
                j=j+1
                
    else:
        for i in g:
            if y[i] in x:
                print(y[i])
                i=i+1
            else:  
                i=i+1
                
    return

print(" ")
x=input("First word: ")
y=input("Second word: ")
f=range(len(x))
g=range(len(y))
i=0
j=0
print(" ")
print("Length of ", x,"  is ", len(x))
print("Length of ", y," is ", len(y))


print(" ")
#print("f ", f);
common(x,y)


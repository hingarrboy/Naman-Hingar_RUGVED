s=input("Enter a string: ")
x=list(s)
l=len(x)
for i in range(0,l-1):
    pos=i
    small=x[i]
    for j in range(i+1,l):
       if(x[j]<small):
           pos=j
           small=x[j]
    x[pos]=x[i]
    x[i]=small     
for i in x:
    print(i,end="")

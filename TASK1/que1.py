def triple_and(a,b,c):
   return (a and b and c)

def bool(x):  
    x = x.lower() 
    if x in ("0", "false"):
        return False
    else:
        return True

a=input("Enter True(1) or False(0): ")
b=input("Enter True(1) or False(0): ")
c=input("Enter True(1) or False(0): ")

aa=bool(a)
bb=bool(b)
cc=bool(c)

print(triple_and(aa,bb,cc))
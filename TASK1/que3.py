def hill(num):
    s=str(num)
    n=len(s)
    i=1
    while i<n and s[i]>s[i-1]:
        i+=1
    if i==1 or i==n:
        return False
    while i<n and s[i]<s[i-1]:
           i+=1
    return i==n
a=int(input("ENTER NUMBER: "))
b=hill(a)
if b==True:
     print("IT IS A HILL NUMBER")
else:
     print("IT IS NOT A HILL NUMBER")
x=input("Enter the string: ")
xx=sorted(x)
print("The sorted array in alphabetical order is: ")
for i in range(0,len(x)):
     print(xx[i], end="")

print("")
for i in set(xx):
    print(i+": "+ str(x.count(i)))
    
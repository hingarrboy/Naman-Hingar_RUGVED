n=int(input("Enter the number of terms: "))
a=0
b=1
print("Fibonacci Series:")
for i in range(0,n):
    print(a,end=" ")
    a,b=b,a+b

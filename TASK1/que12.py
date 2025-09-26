n = int(input("Enter the range: "))
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
for i in range(n-1,-1,-1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


for i in range(n,0,-1):
    for j in range(1,i+1):
        print("* ",end="")
    for j in range(1,2*(n-i)+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*", end=" ")
    print()

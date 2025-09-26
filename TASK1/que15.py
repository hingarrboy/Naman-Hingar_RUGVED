n=int(input("Enter the size of the matrix (n): "))
matrix=[]
print("Enter the elements row by row:")
for i in range(n):
    row=list(map(int, input().split()))
    matrix.append(row)
for i in range(n):
    for j in range(i,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for i in range(n):
    matrix[i].reverse()
top,bottom,left,right=0,n - 1,0,n - 1
print("Spiral order of rotated matrix:")
while top<=bottom and left<=right:
    for i in range(left,right+1):
        print(matrix[top][i],end=" ")
    top+=1
    for i in range(top, bottom+1):
        print(matrix[i][right],end=" ")
    right-=1
    if top<=bottom:
        for i in range(right,left-1,-1):
            print(matrix[bottom][i], end=" ")
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):
            print(matrix[i][left],end=" ")
        left+=1
s=input("Enter string: ")
n=int(input("Enter the number of characters per part: "))
if len(s)%n!=0:
    print("Error:string cannot be divided into equal parts of length", n)
else:
    first=s[0:n]
    i=0
    can_divide = True
    while i<len(s):
        current=s[i:i+n]
        if current!=first:
            can_divide=False
            break
        i+=n
    if can_divide:
        print("The divided parts are:")
        i=0
        while i<len(s):
            print(s[i:i+n])
            i+=n
    else:
        print("Error: All parts are not identical")

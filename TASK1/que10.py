num=input("ENTER CARD NUMBER:")
num=num.replace(" ", "").replace("-", "")
total = 0
length = len(num)
if not num.isdigit():
    print("Invalid input. Not a number.")
    exit()
for i in range(length):
    digit = int(num[length - 1 - i])
    if i % 2 == 1:
        digit *= 2
        if digit > 9:
            digit -= 9
        
    total += digit
grtotal=total % 10
if grtotal==0:
    print("Credit card is VALID")
else:
    print("Credit card is INVALID")

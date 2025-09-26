text=input("Enter text: ")
letters=0
for char in text:
    if char.isalpha(): 
        letters+=1
words=0
for char in text:
    if char==" ":
        words+=1
words+=1
sentences = 0
for char in text:
    if char in ".!?":
        sentences+=1
index=0.0588*(letters/words*100)-0.296*(sentences/words*100)-15.8
grade = round(index)
if (grade<1):
    print("LOWER THAN 1")
else:
    print("Grade", grade)
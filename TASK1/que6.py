s1=input("Enter string 1: ")
s2=input("Enter string 2: ")
s1=sorted(s1)
s2=sorted(s2)
if s1==s2:
    print("The given strings are anagrams")
else:
    print("The given strings are not anagrams")   
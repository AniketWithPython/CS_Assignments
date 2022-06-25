#to check whether input string is palindrome or not
str1=input("Enter string: ")
str1=str1.lower()
a=len(str1)
str2=''
for i in range(a-1,-1,-1):
    str2+=str1[i]
print()
if str2==str1:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
    
    

#find no. of uppercase and lowercase characters
str1=input("Enter desired string to check: ")
u=0
l=0
for i in str1:
    if i.isupper()==True:
        u+=1
    elif i.islower()==True:
        l+=1
print("No. of uppercase characters:",u)
print("No. of lowercase characters:",l)

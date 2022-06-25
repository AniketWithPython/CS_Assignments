#count number of vowels in string
str1=input("Enter string: ")
v=0
for i in str1:
    if i in 'aeiouAEIOU':
        v+=1
print("No. of vowels:",v)

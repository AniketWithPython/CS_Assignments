#reverse all words in string
str1=input("Enter desired string: ")
a=str1.split()
c=len(a)
str2=''
for i in range(c-1,-1,-1):
    x=a[i].replace('.','')
    str2+=x+' '
print()
print(str2)


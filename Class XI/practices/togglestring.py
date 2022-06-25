#read a string and return by capitalizing alternate letters
str1=input("Enter string: ")
a=len(str1)
print()
for i in range(a):
    if i%2==0:
        print(str1[i].upper(),end='')
    else:
        print(str1[i].lower(),end='')


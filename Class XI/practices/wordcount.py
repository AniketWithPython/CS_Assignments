#count number of words in a sentence
str1=input("Enter desired string: ")
a=str1.split()
c=0
for i in a:
    c+=1
print()
print("No. of words is:",c)

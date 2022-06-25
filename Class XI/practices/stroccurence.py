#reads a line and then counts how many times a substring "is" appears in the line
str1=input("Enter desired string: ")
str1=str1.lower()
ar=str1.split()
c=0
for i in ar:
    if i=='is':
        c+=1
print()
print("The string \"is\" occurs",c,"times")

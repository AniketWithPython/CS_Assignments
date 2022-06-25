#remove elem from dict
d={}
n=int(input("Enter no. of entries: "))
for i in range(n):
    key=input("Enter key: ")
    val=input("Enter Value: ")
    d[key]=val
print("Dictionary is:",d)
rem=input("Enter key of entry to be removed: ")
if rem in d.keys():
    del d[rem]
    print("Modified dictionary is:",d)
else:
    print("ERROR: Key not found")
    


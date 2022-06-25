l=[3,21,5,6,14,8,14,3]
print(l)
s=len(l)
i=0
while i<s:
    if l[i]%7==0:
        l[i],l[i+1]=l[i+1],l[i]
        i+=2
    else:
        i+=1
print(l)

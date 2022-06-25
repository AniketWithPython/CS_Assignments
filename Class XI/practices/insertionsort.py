#Insertion sort
l=[70,49,31,6,65,81,68]
t=0
print("Before sorting:",l)
for i in l:
    j=l.index(i)
    while j>0:
        if l[j-1]>l[j]:
            t=l[j-1]
            l[j-1]=l[j]
            l[j]=t
        else:
            break
        j=j-1
print("list after sorting:",l)

#Bubble sort
l=[52,39,75,9,85,55]
x=len(l)
t=0
print("Before sorting:\n",l,sep='')
for i in range(x-1):
    for j in range(x-i-1):
        if l[j]>l[j+1]:
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t
print("After sorting:\n",l,sep='')

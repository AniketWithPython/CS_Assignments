#create list with few elements and sort in descending order
n=int(input("Enter no. of elements: "))
l=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)

print("Before sorting:\n",l,sep='')

a=len(l)
for i in range(a-1):
    for j in range(a-i-1):
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print("After arranging:\n",l,sep='')

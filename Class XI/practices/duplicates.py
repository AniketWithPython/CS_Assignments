#create list with few elements and display duplicate elements in a list
n=int(input("Enter no. of elements: "))
l=[]
m=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
print("List is:\n",l,sep='')

for j in l:
    if l.count(j)>1:
        if j not in m:
            m.append(j)
print("Duplicate elements:\n",m,sep='')
    

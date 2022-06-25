'''create a list with few elements and to find and display the sum
of all the values which are ending with 3. Also display list items.'''

n=int(input("Enter no. of elements in a list: "))
l=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
print("list is:\n",l,sep='')
s=0
for j in l:
    k=j
    while k>10:
        k=j%10
    if k==3:
        s+=j
print("Sum of all values ending with 3:",s)
        
        
    


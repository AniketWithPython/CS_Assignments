'''Exchange first half elements of list with 2nd half
elements of list assuming list is having even no. of elements
e.g [10,20,30,40,50,60,70] -> [40,50,60,10,20,30,70]'''

#NEEDS MODIFICATION!!

n=int(input("Enter no. of elements: "))
l=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
print("Original List:\n",l,sep='')

m=len(l)
if m%2!=0:
    m-=1
for j in range(m//2):
    l[j],l[m-j]=l[m-j],l[j]
print("After processing:\n",l,sep='')

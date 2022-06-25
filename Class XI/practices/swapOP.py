'''create a list with few elements and rearrange the list in such a way that
the values of alternate locations of the list are exchanged. size of list is always even
e.g [2,5,9,14,17,8,19,16] -> [5,2,14,9,8,17,16,19]'''
while True:
    n=int(input("Enter no. of elements(must be even): "))
    if n%2==0:
        break
    else:
        print("ERROR")

l=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
print("List is:\n",l,sep='')
j=0
while j<len(l):
    l[j],l[j+1]=l[j+1],l[j]
    j+=2
print("After processing:\n",l,sep='')

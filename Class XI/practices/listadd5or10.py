'''create a list with n no. of elements and add 5 in all odd values
and add 10 in all even values of the list'''
n=int(input("Enter no. of elements: "))
l=[]
for i in range(n):
    a=int(input("Enter integer element: "))
    l.append(a)
print("\nBefore formatting:")
print(l)
for i in range(len(l)):
    if l[i]%2==0:
        l[i]+=10
    else:
        l[i]+=5
print("\nAfter formatting:")
print(l)

        
    
    

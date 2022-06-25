#create tuple and delete the elements given by user
n=int(input("Enter no. of elements: "))
tup=()
for i in range(n):
    elem=input("Enter element: ")
    tup+=(elem,)
rem=input("Enter element to be removed:")
print("Original Tuple:",tup)
tup=list(tup)
a=len(tup)
n=0
while n<a:
    if tup[n].upper()==rem.upper():
        del tup[n]
        a-=1
    else:
        n+=1
tup=tuple(tup)
print("Modified Tuple:",tup)


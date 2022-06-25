#swap values of 2 tuples
n1=int(input("Enter no. of elements in first tuple: "))
t1=()
for i in range(n1):
    x=int(input("Enter element: "))
    t1+=(x,)
print()
n2=int(input("Enter no. of elements in second tuple: "))
t2=()
for i in range(n2):
    x=int(input("Enter element: "))
    t2+=(x,)
print()
print("Before swapping tuples are:",t1,t2,sep="\n")
t1,t2=t2,t1
print("After swapping tuples are:",t1,t2,sep="\n")

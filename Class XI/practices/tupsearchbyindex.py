#input few elements in tuple and display searched element by index no.
t=()
n=int(input("Enter no. of elements: "))
for i in range(n):
    elem=input("Enter element: ")
    t+=(elem,)
print("Tuple is:",t)
search=int(input("Enter index of element: "))
if search<len(t):
    result=t[search]
    print("Result is:",result)
else:
    print("ERROR: Index out of range")

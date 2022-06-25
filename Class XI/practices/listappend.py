#Add n number of elements(integers, string, float) in a list
n=int(input("Enter no. of elements to add: "))
l=[]
for i in range(n):
    a=input("Enter element: ")
    l.append(a)
print("\nThe list is now:")
print(l)

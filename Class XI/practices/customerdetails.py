#Customer details
d={}
ID=int(input("Enter customer ID: "))
d["ID"]=ID
n=int(input("Enter no. of items: "))
ph=int(input("Enter phone no.: "))
d["phone"]=ph
items=[]
for i in range(n):
    name=input("Enter name of item: ")
    qty=int(input("Enter quantity: "))
    cost=int(input("Enter cost of items: "))
    items.append((name,qty,cost))
d['items']=items
print()
print("Customer ID:",d["ID"])
print("Customer Phone no.:",d["phone"])
print()
print("{:<10}{:<15}{}\n\n".format('Name','Quantity','Cost'))
for i in d['items']:
    print("{:<10}{:<15}{}\n".format(i[0],i[1],i[2]))
print()
total=0
for i in d['items']:
    total+=i[1]*i[2]
print("Total cost:",total)

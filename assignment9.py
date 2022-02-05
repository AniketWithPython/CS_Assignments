#Assignment-9
while True:
    x,y,z=[],[],[]

    #size and element input
    m=int(input("Enter size of list x:"))  
    for i in range(m):
        elem=int(input("Enter element:"))
        x.append(elem)

    n=int(input("Enter size of list y:"))
    for i in range(n):
        elem=int(input("Enter element:"))
        y.append(elem)

    #creation of list z
    for i in x:
        if i%2!=0:
            z.append(i)
    for i in y:
        if i%2!=0:
            z.append(i)
    x.reverse()
    y.reverse()
    for i in y:
        if i%2==0:
            z.append(i)
    for i in x:
        if i%2==0:
            z.append(i)
    x.reverse()
    y.reverse()  

    #final output
    print("Original lists:\n","x:",x,"\n","y:",y)
    print("New list z:",z)
    yn=input("\nDo you want to continue?(y/n): ")
    if yn in 'Nn':
        break

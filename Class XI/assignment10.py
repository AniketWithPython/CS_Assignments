#Assignment 10
while True:
    a,b,c=[],[],[]

    #size and element input
    m=int(input("Enter size of list a: "))
    for x in range(m):
        elem=int(input("Enter element: "))
        a.append(elem)

    n=int(input("Enter size of list b: "))
    for x in range(n):
        elem=int(input("Enter element: "))
        b.append(elem)

    #creation of list z
    for i in a:
        if i%2==0:
            c.append(i)
    for i in b:
        if i%2==0:
            c.append(i)
    a.reverse()
    b.reverse()
    for i in b:
        if i%2!=0:
            c.append(i)
    for i in a:
        if i%2!=0:
            c.append(i)
    a.reverse()
    b.reverse()

    #final output
    print("Original lists:\n","a:",a,"\n","b:",b)
    print("New list c:",c)
    yn=input("\nDo you want to continue?(y/n): ")
    if yn in 'Nn':
        break

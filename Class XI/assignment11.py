#Assignment 11
while True:
    choice=input("Enter option(I/i for tuple interchange or D/d for value deletion): ")
    if choice in 'Ii':
        #tuple interchange
        a,b=(),()
        n=int(input("\nEnter size of first tuple: "))
        for i in range(n):
            elem=int(input("Enter element: "))
            a+=(elem,)
        n=int(input("Enter size of second tuple: "))
        for i in range(n):
            elem=int(input("Enter element: "))
            b+=(elem,)
        print("Tuples before swapping:\n","a: ",a,"\n","b: ",b,sep='')
        a,b=b,a
        print("Tuples after swapping:\n","a: ",a,"\n","b: ",b,sep='')
    elif choice in 'Dd':
        #value deletion 
        n=int(input("\nEnter size of tuple: "))
        tup=()      
        for i in range(n):
            elem=int(input("Enter element: "))
            tup+=(elem,)
        print("Tuple is:",tup)
        rem=int(input("Enter value to be removed: "))
        tup=list(tup)
        ind=tup.count(rem)
        for i in range(ind):
            tup.remove(rem)
        tup=tuple(tup)
        print("After removing:",tup)
    else:
        print("\nError invalid input, try again\n")
        continue    
    yn=input("Do you want to continue?: ")
    if yn in 'Nn':  
        break
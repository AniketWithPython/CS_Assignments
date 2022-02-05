x='y'
while x=='Y' or x=='y':
    
    #user input with error check
    while True:
        a=input("choose pattern (S/s for star triangle or N/n for number arch: ")
        if a in['S','s','N','n']:
            break
        else:
            print("ERROR: Invalid Input. Try Again")
            print()
            
    n=int(input("Enter parameter. Must be Integer: "))
    print()
    
    if a=='S' or a=='s':
        # star (*) triangle
        i=0
        while i<=n-1:
            j=0
            while j<=i:
                print("*",end=' ')
                j=j+1
            i+=1
            print()
        while 1<i<=n:
            j=i-1
            while j>0:
                print("*",end=' ')
                j-=1
            i-=1
            print()
    
    elif a=='N' or a=='n':
        #number arch
        for j in range(1,n+1):
            for i in range(0,n):
                if n-i>=j:
                    print(n-i,end=' ')
                else:
                    print(" ",end=' ')
            for i in range(1,n+1):
                if i>=j:
                    print(i,end=' ')
                else:
                    print(" ",end=' ')
            print()
    
    x=input("Do you want to continue? (press Y/y): ")

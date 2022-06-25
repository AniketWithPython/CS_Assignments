'''
print like
1
2 2
3 3 3
4 4 4 4
and so on
'''
n=int(input("Enter number: "))
i=0
while(i<=n):
    j=1
    while(j<=i):
        print(i,end=' ')
        j=j+1
    print()
    i=i+1

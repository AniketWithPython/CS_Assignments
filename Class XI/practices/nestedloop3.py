'''
print like
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
and so on
'''
n=int(input("Enter: "))
i=1
while(i<=n):
    j=1
    while(j<=i):
        print(i-j+1,end=' ')
        j=j+1
    print()
    i=i+1

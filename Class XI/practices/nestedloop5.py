'''
1 2 3 4 5 6 7
1 2 3 4 5
1 2 3
1
'''
i=0
while (i<=7):
    j=1
    while (j<=7-i):
        print(j, end=' ')
        j+=1
    i+=2
    print()

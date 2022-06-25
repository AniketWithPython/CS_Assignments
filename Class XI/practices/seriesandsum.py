'''
Display series and its sum upto n terms
x*1/1!+x*2/2+x*3/3!...x^n/n!
'''
x=int(input("Enter x: "))
n=int(input("Enter no. of terms: "))
sum=0
for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
        f=f*j
    print(x**i/f,end=' ')
    sum=sum+(x**i/f)
print()
print("Sum is:",sum)



#find series and sum; a/a^2, a^2/a^3, a^3/a^4....n terms
sum=0
a=int(input("enter a: "))
n=int(input("enter no. of terms: "))
for i in range(0,n):
    t=(a**i)/(a**(i+1))
    print(t, end=' ')
    sum=sum+t
print()
print("sum is",sum)

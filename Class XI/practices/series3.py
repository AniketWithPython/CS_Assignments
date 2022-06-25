#Display series and its sum upto n terms: 1/2+2/3+3/4....nterms
sum=0
n=int(input("Enter no. of terms: "))
for i in range(1,n+1):
    x=i/(i+1)
    sum=sum+x
    print(x,end=', ')
print()
print("sum is:",sum)

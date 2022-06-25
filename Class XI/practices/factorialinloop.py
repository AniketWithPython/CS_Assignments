#factorial of n
n=int(input("Enter n: "))
f=1
for i in range(1,n+1):
    f=f*i
    print("i =",i,"f =",f)
print()
print(n,"! is = ",f,sep='')

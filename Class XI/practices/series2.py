#To display series and its sum (1*2+2*3.....19*20)
sum=0
for i in range(1,20):
    t=i*(i+1)
    sum=sum+t
    print(t,end=' ')
print(end='\n')
print("Sum is:",sum)

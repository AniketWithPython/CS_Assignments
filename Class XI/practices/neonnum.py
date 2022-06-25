'''
enter no. and check whether neon no. or not
(e.g for 9, 9^2=81, 8+1=9)
'''
n=int(input("Enter number: "))
n1=n
sum=0
n=n**2
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
if n1==sum:
    print("Neon number")
else:
    print("Not neon number")

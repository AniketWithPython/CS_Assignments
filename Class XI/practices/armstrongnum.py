'''
enter no. and check whether armstrong number or not
(e.g for 153, 1^3+5^3+3^3=153
'''
n=int(input("Enter number: "))
x=n
d=0
sum=0
while n>0:
    d=n%10
    cube=d**3
    sum=sum+cube
    n=n//10
if x==sum:
    print("Armstrong number")
else:
    print("Not armstrong number")

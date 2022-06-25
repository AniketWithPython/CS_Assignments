'''
to check if a number is a perfect number
(a number is perfect if it is equal to the sum of its factors other than the number itself)
(e.g 6,28,496,8128)
'''
n=int(input("Enter number to check: "))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n:
    print("perfect number")
else:
    print("not perfect number")

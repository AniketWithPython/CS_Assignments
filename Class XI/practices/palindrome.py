'''
check whether a number is palindrome or not
(if original and reverse number is same)
'''
n=int(input("enter number: "))
rev=0
n1=n
while n>0:
    d=n%10
    rev=rev*10+d
    n=int(n/10)
if n1==rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
    

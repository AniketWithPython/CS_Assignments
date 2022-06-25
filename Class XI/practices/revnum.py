#reverse the order of digits (eg 123 -> 321)
n=int(input("Enter number: "))
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=int(n/10)
print("Reverse number is:",rev)

'''To accept number and check:
whether number divisible by 2 and 5
whether number divisible by 2 but not 5
whether number divisible by 5 but not 2'''
x=int(input("enter a positive integer: "))
if x%2==0 and x%5==0:
    print("number divisible by 2 and 5")
elif x%2==0:
    print("number divisible by 2 but not 5")
elif x%5==0:
    print("number divisible by 5 but not 2")
else:
    print("number divisible by neither 2 or 5")

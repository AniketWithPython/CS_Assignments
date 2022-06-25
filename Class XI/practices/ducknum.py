'''
a number is said to be duck number if the digit zero is present in it.
accept a number and check whether a number is duck number or not
'''
n=int(input("enter number: "))
mark=0
while n>0:
    d=n%10
    n=n//10
    if d==0:
        mark=1       #flagging if digit zero is found
        break
if mark==1:
    print("Duck number")
else:
    print("Not a duck number")
    

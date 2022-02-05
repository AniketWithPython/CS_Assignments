x='y'
while x=='y' or x=='Y':

    while True:   #test input with error check
        a=input("Enter test mode (P/p for palindrome test or A/a for Armstrong number test): ")
        if a in['P','p','A','a']:
            break
        else:
            print("ERROR: Invalid Input. Try Again")

    n=int(input("Enter number to check: "))

    if a=='P' or a=='p':   #palindrome test
        rev=0
        n1=n
        while n>0:
            d=n%10
            rev=rev*10+d
            n=n//10
        if n1==rev:
            print("It is a palindrome")
        else:
            print("It is not a palindrome")

    elif a=='A' or a=='a':  #armstrong num test
        arm=n
        e=0
        sum=0
        while n>0:
            e=n%10
            cube=e**3
            sum=sum+cube
            n=n//10
        if arm==sum:
            print("It is an armstrong number")
        else:
            print("It is not an armstrong number")

    print()
    x=input("Do you want to continue? (Press Y/y): ")
    print()



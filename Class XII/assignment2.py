#assignment2
def ARMSTRONG(num:int):     #to check armstrong number
    c=0
    num1=num
    while num>0:
        d=num%10
        c+=d**3
        num//=10
    if num1==c:
        print(num1,"is an armstrong number")
    else:
        print(num1,"is not an armstrong number")

def PALIN(st:str):      #to check palindrome string
    if st==st[::-1]:
        print(st,"is a palindrome")
    else:
        print(st,"is not a palindrome")
    
def main():
    while True:
        choice=input("Enter A/a for armstrong number check or P/p for palindrome string test: ")
        if choice in "Aa":      #armstrong num check
            i=int(input("Enter number to check: "))
            ARMSTRONG(i)
            
        elif choice in "Pp":    #palindrome string check
            s=input("Enter string to check: ")
            PALIN(s)
            
        else:
            print("Invalid input. Try again")
            continue
        
        yn=input("Do you want to continue?(y/n): ")
        if yn in "Nn":
            break

if __name__=="__main__":
    main()

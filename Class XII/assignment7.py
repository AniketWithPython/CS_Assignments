from tkinter import N


def SERIES(terms:int):
    ser='1'
    for i in range(2,terms+1):
        ser+=', '+str((-1)**i*1/i)
    print(ser)
    ser='+'.join(ser.split(','))
    print("Sum is:",eval(ser))

def NEON(num:int):
    num1=num
    num**=2
    sum=0
    while num>0:
        sum+=num%10
        num//=10
    if sum==num1:
        print(num1,"Is a neon number")
    else:
        print(num1,"Is not a neon number")

def main():
    while True:
        choice=input("Enter S/s for SERIES or N/n for NEON: ")
        
        if choice in "Ss":
            #SERIES
            n=int(input("Enter number of terms: "))
            SERIES(n)
        elif choice in "Nn":
            #NEON
            n=int(input("Enter number to check: "))
            NEON(n)
        else:
            print("Invalid input. Try again")
            continue

        yn=input("Do you want to continue?(y/n): ")     
        if yn in "Nn":
            break

if __name__=="__main__":
    main()
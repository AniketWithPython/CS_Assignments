#assignment3
def fact(num:int):      #factorial 
    c=1
    fac=1
    while c<num+1:
        fac*=c
        c+=1
    return fac
    
def FACT_SERIES(a:int,terms:int):       #FACT_SERIES function
    c=2
    ser='1'
    while c<terms+1:
        ser+=', '+str(a**c/fact(c-1))
        c+=1
    print("series is:",ser)
    ser='+'.join(ser.split(","))
    print("sum is:",eval(ser))

def NEW_STR(inp:str):       #NEW_STR function e.g Subhash Bose -> S Bose
    l=inp.split()
    out=''
    for i in range(len(l)-1):
        out+=l[i][0]+'.'
    out+=l[-1]
    print(out)

def main(): 
    while True:
        choice=input("Enter F/f for FACT_SERIES or N/n for NEW_STR: ")      #user choice

        if choice in "Ff":
            #FACT_SERIES
            p=int(input("Enter parameter a: "))
            t=int(input("Enter no. of terms: "))
            FACT_SERIES(p,t)
            
        elif choice in "Nn":
            #NEW_STR
            str1=input("Enter string: ")
            NEW_STR(str1)

        else:
            print("Invalid input. Try again")
            continue

        yn=input("Do you want to continue?(y/n): ")     
        if yn in "Nn":
            break

if __name__=="__main__":
    main()


#assignment11
def P_INSERT(p_no,p_name,p_score,p_amount,fileobj):
    data=",".join([p_no,p_name,p_score,p_amount])+"\n"
    fileobj.write(data)
    
def P_DISP(fileobj):
    print("{:<12}{:<12}{:<12}{}\n".format("p_no","p_name","p_score","p_amount"))
    for line in fileobj:
        r=line.split(',')       #delimiter is comma
        print("{:<12}{:<12}{:<12}{}\n".format(r[0],r[1],r[2],r[3]),end='')

def P_COPY(fileobj):
    with open("./pcsports.txt","w") as f:
        for line in fileobj:
            if int(line.split(',')[3])>=300000:     #4th field is p_amount
                f.write(line)
                
def P_SEARCH(search,fileobj):
    rec=[]
    for line in fileobj:
        if line.split(',')[0]==search:      #1st field is p_no.
            rec.append(line)
    if len(rec)==0:
        print("Sorry no records found")
        return
    else:
        print("{:<12}{:<12}{:<12}{}\n".format("p_no","p_name","p_score","p_amount"))
        for i in rec:
            r=i.split(',')
            print("{:<12}{:<12}{:<12}{}\n".format(r[0],r[1],r[2],r[3]),end='')

def main():
    yn='y'
    while yn in 'yY':
        choice=input('''Enter option
1. P_INSERT
2. P_DISP
3. P_COPY
4. P_SEARCH
''')
        if choice=='1':
            ans='y'
            with open("./psports.txt","w") as f:
                while ans in "Yy":
                    no=input("Enter player number:")
                    name=input("Enter player name:")
                    score=input("Enter player score:")
                    amt=input("Enter player monthly amount:")
                    P_INSERT(no,name,score,amt,f)
                    ans=input("Add more?(y/n):")
                    
        elif choice=='2':
            with open("./psports.txt","r") as f:
                P_DISP(f)
        elif choice=='3':
            with open("./psports.txt","r") as f:
                P_COPY(f)
        elif choice=='4':
            s=input("Enter player no. to search:")
            with open("./psports.txt","r") as f:
                P_SEARCH(s,f)
        else:
            print("Invalid input. Try again")
            continue

        yn=input("Do you want to continue?(y/n):")

main()
        
                

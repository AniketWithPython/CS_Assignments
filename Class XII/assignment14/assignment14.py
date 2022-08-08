#assignment14
#----------------------IGNORE (for system purposes only)---------------------
from os import chdir
chdir(r'C:\Users\Student\Desktop\CS CW\assignmentx')
#----------------------------------------------------------------------------

import csv

def add(data,fileobj):
    writer=csv.writer(fileobj,lineterminator='\n')
    for i in data:
        writer.writerow(i)

def show(fileobj):
    data=fileobj.readlines()
    print("{:<12}{:<12}{:<12}{:<12}{}".format('c_no','c_name','c_areacode','c_phoneno','c_bill\n'))
    for i in data:
        r=i.split(",")
        print("{:<12}{:<12}{:<12}{:<12}{}".format(r[0],r[1],r[2],r[3],r[4]))           

def search(search,fileobj):
    test=True
    rec=fileobj.readlines()
    for i in rec:
        r=i.split(",")
        if r[0]==search:
            print("{:<12}{:<12}{:<12}{:<12}{}\n".format('c_no','c_name','c_areacode','c_phoneno','c_bill'))
            print("{:<12}{:<12}{:<12}{:<12}{}".format(r[0],r[1],r[2],r[3],r[4]))
            test=False
    if test:
        print("Sorry no records found")

def main():
    yn='y'
    while yn in 'yY':
        choice=input("Enter function to use (1.add,2.show,3.search): ")
        if choice=='1':
            ans='y'
            dat=[]
            while ans in 'yY':
                no=input("Enter consumer no.: ")
                name=input("Enter consumer name: ")
                code=input("Enter consumer area code: ")
                phno=input("Enter consumer phoneno.: ")
                bill=input("Enter consumer bill: ")
                dat.append([no,name,code,phno,bill])
                ans=input("add more?:")
            with open("./tele.csv",'w') as f:
                add(dat,f)
        elif choice=='2':
            with open("./tele.csv") as f:
                show(f)
        elif choice=='3':
            with open("./tele.csv") as f:
                s=input("Enter consumer no.: ")
                search(s,f)        
        else:
            print("Invalid input. Try again")
            continue
        yn=input("Do you want to continue?(y/n):")

main()

#assignment12
import pickle as pkl
def c_insert(data,fileobj):
    pkl.dump(data,fileobj)

def c_disp(fileobj):
    print("{:<12}{:<12}{:<12}{:<12}{}".format('c_no','c_name','c_areacode','c_phoneno','c_bill'))
    rec=pkl.load(fileobj)
    for r in rec:
        print("{:<12}{:<12}{:<12}{:<12}{}".format(r[0],r[1],r[2],r[3],r[4]))

def c_append(olddata,data,fileobj):
    data+=olddata
    pkl.dump(data,fileobj)

def c_search(search,fileobj):
    test=True
    rec=pkl.load(fileobj)
    for r in rec:
        if r[0]==search:
            print("{:<12}{:<12}{:<12}{:<12}{}\n".format('c_no','c_name','c_areacode','c_phoneno','c_bill'))
            print("{:<12}{:<12}{:<12}{:<12}{}".format(r[0],r[1],r[2],r[3],r[4]))
            test=False
    if test:
        print("Sorry no records found")

def c_copy(fileobj):
    data=pkl.load(fileobj)
    copy=[]
    for r in data:
        if r[2]=='03222':
            copy.append(r)
    with open('./teleback.dat','wb') as f:
        pkl.dump(copy,f)
    print("data copied successfully")
    c_disp(open('./teleback.dat','rb'))

def main():
    yn='y'
    while yn in 'yY':
        choice=input("Enter function (1.c_insert,2.c_disp,3.c_append,4.c_search,5.c_copy): ")
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
            with open('./telephone.dat','wb') as f:
                c_insert(dat,f)
        elif choice=='2':
            with open('./telephone.dat','rb') as f:
                c_disp(f)
        elif choice=='3':
            f=open('./telephone.dat','rb')
            odat=pkl.load(f)
            f.close()
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
            with open('./telephone.dat','wb') as f:
                c_append(odat,dat,f)
        elif choice=='4':
            with open('./telephone.dat','rb') as f:
                s=input("Enter consumer no.: ")
                c_search(s,f)
        elif choice=='5':
            with open('./telephone.dat','rb') as f:
                c_copy(f)
        else:
            print("Invalid input try again")
            continue
        yn=input("Do you want to continue?(y/n): ")

main()

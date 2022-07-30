import pickle as pkl
def s_insert(data,fileobj):
    pkl.dump(data,fileobj)
def s_disp(fileobj):
    print("{:<12}{:<12}{:<12}{:<12}{}".format('s_no','s_name','s_rollno','s_total_marks','s_per'))
    rec=pkl.load(fileobj)
    for r in rec:
        print("{:<12}{:<12}{:<12}{:<12}{}".format(r[0],r[1],r[2],r[3],r[4]))
def s_search(search,fileobj):
    test=True
    rec=pkl.load(fileobj)
    for r in rec:
        if r[0]==search:
            print("{:<12}{:<12}{:<12}{:<12}{}\n".format('s_no','s_name','s_rollno','s_total_marks','s_per'))
            print("{:<12}{:<12}{:<12}{:<12}{}".format(r[0],r[1],r[2],r[3],r[4]))
            test=False
    if test:
        print("Sorry no records found")
def s_update(data,fileobj):
    for r in data:
        if 155<=r[3]<165:
            r[3]+=10
    pkl.dump(data,fileobj)
    print("Updated successfully")
    s_disp(open('./student.dat','rb'))
def s_copy(fileobj):
    data=pkl.load(fileobj)
    copy=[]
    for r in data:
        if r[4]>='90':
            copy.append(r)
    with open('./student_top.dat','wb') as f:
        pkl.dump(copy,f)
    print("data copied succesfully")
    s_disp(open('./student_top.dat','rb'))
def main():
    yn='y'
    while yn in 'yY':
        choice=input("Enter function (1.s_insert,2.s_disp,3.s_search,4.s_update,5.s_copy): ")
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

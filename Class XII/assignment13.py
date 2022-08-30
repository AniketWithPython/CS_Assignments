#assignment13
import pickle as pkl
def s_insert(data,fileobj):
    pkl.dump(data,fileobj)

def s_disp(fileobj):
    print("{:<12}{:<12}{:<12}{:<14}{}".format('s_adno','s_name','s_rollno','s_total_marks','s_per'))
    try:
        rec=pkl.load(fileobj)
    except EOFError:
        print("No data")
        return
    for r in rec:
        print("{:<12}{:<12}{:<12}{:<14}{}".format(r[0],r[1],r[2],r[3],r[4]))

def s_search(search,fileobj):
    test=True
    try:
        rec=pkl.load(fileobj)
    except EOFError:
        print("No data")
        return
    for r in rec:
        if r[0]==search:
            print("{:<12}{:<12}{:<12}{:<14}{}\n".format('s_adno','s_name','s_rollno','s_total_marks','s_per'))
            print("{:<12}{:<12}{:<12}{:<14}{}".format(r[0],r[1],r[2],r[3],r[4]))
            test=False
    if test:
        print("Sorry no records found")

def s_update(data,fileobj):
    for r in data:      #update records
        if 155<=r[3]<165:
            r[3]+=20
            r[4]=r[3]*0.2
    pkl.dump(data,fileobj)      #write updated data
    fileobj.close()
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
                adno=input("Enter admission no.: ")
                name=input("Enter name: ")
                rno=input("Enter roll no.: ")
                marks=int(input("Enter total marks(out of 500): "))
                perc=marks*0.2
                dat.append([adno,name,rno,marks,perc])
                ans=input("add more?:")
            with open('./student.dat','wb') as f:
                s_insert(dat,f)
        elif choice=='2':
            with open('./student.dat','rb') as f:
                s_disp(f)
        elif choice=='3':
            with open('./student.dat','rb') as f:
                n=input("Enter admission no.: ")
                s_search(n,f)
        elif choice=='4':
            f=open('./student.dat','rb')
            dat=pkl.load(f)     #retrive data
            f.close()
            with open('./student.dat','wb') as f:
                s_update(dat,f)
        elif choice=='5':
            with open('./student.dat','rb') as f:
                s_copy(f)
        else:
            print("Invalid input try again")
            continue
        yn=input("Do you want to continue?(y/n): ")

main()

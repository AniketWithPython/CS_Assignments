Empdict={}
while True:
    choice=input('''1. store data in dictionary
2. display employee details
3. display the details of all employees whose  Gross Pay  more  than  equal  to  1000000  and  display  the  number  of 
Employee's GrossPay more than equal to 1000000
4. Update the BasicPay by increasing 10% \of BasicPay  for those employee's whose BasicPay is less than 20000 and 
display the details using tabular form
5. Copy  the Employee's details (Empdict)  whose  Age  is  more  than  60  to  another  dictionary  (Retddict)  and  display  the  details 
using tabular form after copy
6. Delete the Employee's details (Empdict) whose Age is more than 60 and display the details using tabular form after deletion

Enter desired Option: ''')

    if choice=='1':
        n=int(input("Enter no. of entries: "))
        for i in range(n):
            Emp_no=int(input("Enter Emp_no: "))
            Emp_name=input("Enter Emp_name: ")
            Emp_Age=int(input("Enter Emp_Age: ")) 
            Emp_BasicPay=int(input("Enter Basic Pay: "))
            Emp_DA=Emp_BasicPay*(130/100)
            Emp_HRA=Emp_BasicPay*(20/100)
            Emp_CA=Emp_BasicPay*(10/100)
            Emp_MA=Emp_BasicPay*(10/100)
            Emp_PF=Emp_BasicPay*(25/100)
            Emp_GrossPay=Emp_BasicPay+Emp_DA+Emp_HRA+Emp_CA+Emp_MA
            Emp_NetPay=Emp_GrossPay-Emp_PF
            Emp_AI=Emp_NetPay*12
            if Emp_AI<=250000:
                Emp_IT=0
            elif 250001<=Emp_AI<=500000:
                Emp_IT=Emp_AI*(5/100)
            elif 500001<=Emp_AI<=1000000:
                Emp_IT=Emp_AI*(10/100)
            elif 1000001<=Emp_AI<=1250000:
                Emp_IT=Emp_AI*(15/100)
            elif 1250001<=Emp_AI<=1500000:
                Emp_IT=Emp_AI*(20/100)
            else:
                Emp_IT=Emp_AI*(25/100)
            Empdict[Emp_no]=(Emp_name,Emp_Age,Emp_BasicPay,Emp_DA,Emp_HRA,Emp_CA,Emp_MA,Emp_PF,Emp_GrossPay,Emp_NetPay,Emp_AI,Emp_IT)

    elif choice=='2':
        print("{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{}\n".format('ID','Name','Age','Basic_pay','DA','HRA','CA','MA','PF','Gross_Pay','Net_Pay','AI','IT'))
        for i in Empdict.keys():
            dt=Empdict[i]
            print("{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{}".format(i,dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9],dt[10],dt[11]))

    elif choice=='3':
        print("{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{}\n".format('ID','Name','Age','Basic_pay','DA','HRA','CA','MA','PF','Gross_Pay','Net_Pay','AI','IT'))
        c=0
        for i in Empdict.keys():
            dt=Empdict[i]
            if dt[8]<1000000:
                continue
            print("{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{}".format(i,dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9],dt[10],dt[11]))
            c+=1
        print("No. of employees whose gross pay more than equal to 1000000:",c)
    
    elif choice=='4':
        print("{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{}\n".format('ID','Name','Age','Basic_pay','DA','HRA','CA','MA','PF','Gross_Pay','Net_Pay','AI','IT'))
        for i in Empdict.keys():
            dt=Empdict[i]
            if dt[2]<20000:
                dt=list(dt)
                dt[2]*=(110/100)
                dt=tuple(dt)
            print("{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{}".format(i,dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9],dt[10],dt[11]))

    elif choice=='5':
        Retddict={}
        for i in Empdict.keys():
            dt=Empdict[i]
            if dt[1]>60:
                Retddict[i]=dt
        print("{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{}\n".format('ID','Name','Age','Basic_pay','DA','HRA','CA','MA','PF','Gross_Pay','Net_Pay','AI','IT'))
        for i in Retddict.keys():
            dt=Retddict[i]
            print("{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{}".format(i,dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9],dt[10],dt[11]))

    elif choice=='6':
        print("{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{}\n".format('ID','Name','Age','Basic_pay','DA','HRA','CA','MA','PF','Gross_Pay','Net_Pay','AI','IT'))
        for i in Empdict.keys():
            dt=Empdict[i]
            if dt[1]>60:
                del Empdict[i]
        for i in Empdict.keys():
            dt=Empdict[i]
            print("{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{:<8}{:<8}{:<8}{:<11}{:<8}{:<8}{}".format(i,dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9],dt[10],dt[11]))

    else:
        print("Invalid input. Try again\n")
        continue

    yn=input("Do you want to continue?(y/n): ")
    if yn in 'Nn':
        break

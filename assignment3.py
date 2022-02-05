'''
format:
-------------------------------------------------------------------------
                       TSC SOFTWARE SOLUTION LTD.
                              KHARAGPUR
                            03222-220020
-------------------------------------------------------------------------
                             SALARY SLIP
-------------------------------------------------------------------------
Employee’s Number                                   :
Name of the Employee                                :
Designation                                         :
Appointment date                                    :
Address                                             :
Mobile no                                           :
Basic Pay                                           :
Dearness Allowance                                  :
House Rent Allowance                                :
Provident Fund                                      :
Medical Allowance                                   :
Net Pay                                             :
Gross Pay                                           :


-------------------------------------------------------------------------
                      TSC SOFTWARE SOLUTION LTD.
                             KHARAGPUR
                           03222-220020
-------------------------------------------------------------------------
                          INCOME TAX SLIP
-------------------------------------------------------------------------
Employee’s Number                                   :
Name of the Employee                                :
Designation                                         :
Annual Income                                       :
Annual Income Tax                                   :
Monthly Income Tax                                  :

'''

while True:
    print("Enter following details to generate salary slip and income tax slip")
    print()
    n=int(input("Enter number of employees: "))

    for i in range(1,n+1):

        #inputs
        print("Enter employee {} details".format(i))
        empnum=input("Enter employee number : ")
        empname=input("Enter employee name : ")
        desg=input("Enter designation : ")
        appdate=input("Enter appointment date : ")
        addr=input("Enter address : ")
        mobnum=input("Enter mobile number : ")
        bp=int(input("Enter basic pay : "))
        
        #calculations
        da=bp*117/100
        hra=bp*25/100
        pf=bp*12/100
        ma=bp*10/100
        netpay=bp+da+hra+ma
        grosspay=netpay-pf

        #annual income tax calculation
        inc=grosspay*12
        if inc<=150000:
            tax=0
        elif 150001<=inc<=300000:
            tax=(inc-150000)*5/100
        elif 300001<=inc<=500000:
            tax=(150000*5/100)+(inc-300000)*7/100
        elif 500001<=inc<=700000:
            tax=(150000*5/100)+(200000*7/100)+(inc-500000)*7/100
        elif 700001<=inc<=1000000:
            tax=(150000*5/100)+(200000*7/100)+(200000*7/100)+(inc-700000)*9/100
        else:
            tax=(150000*5/100)+(200000*7/100)+(200000*7/100)+(300000*9/100)+(inc-1000000)*10/100

        #output (salary slip)
        print()
        print()
        print("-------------------------------------------------------------------------")
        print("                       TSC SOFTWARE SOLUTION LTD.")
        print("                              KHARAGPUR")
        print("                            03222-220020")
        print("-------------------------------------------------------------------------")
        print("                             SALARY SLIP")
        print("-------------------------------------------------------------------------")
        print("Employee’s Number                                   :",empnum)
        print("Name of the Employee                                :",empname)
        print("Designation                                         :",desg)
        print("Appointment date                                    :",appdate)
        print("Address                                             :",addr)
        print("Mobile no                                           :",mobnum)
        print("Basic Pay                                           :",bp)
        print("Dearness Allowance                                  :",da)
        print("House Rent Allowance                                :",hra)
        print("Provident Fund                                      :",pf)
        print("Medical Allowance                                   :",ma)
        print("Net Pay                                             :",netpay)
        print("Gross Pay                                           :",grosspay)

        #output(income tax slip)
        print()
        print()
        print("-------------------------------------------------------------------------")
        print("                      TSC SOFTWARE SOLUTION LTD.")
        print("                             KHARAGPUR")
        print("                           03222-220020")
        print("-------------------------------------------------------------------------")
        print("                          INCOME TAX SLIP")
        print("-------------------------------------------------------------------------")
        print("Employee’s Number                                   :",empnum)
        print("Name of the Employee                                :",empname)
        print("Designation                                         :",desg)
        print("Annual Income                                       :",inc)
        print("Annual Income Tax                                   :",tax)
        print("Monthly Income Tax                                  :",tax/12)
        print()

    #do you want to continue
    print()
    y=input("Do you want to continue? (Press Y/y): ")
    if y=='y' or y=='Y':
        print()
        pass
    else:
        break

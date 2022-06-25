'''
accept employee names and salaries for n number of employees
and find out no. of emp getting salary as
<20000
>=20000
>=30000
>=50000
'''
n=int(input("Enter number of employees: "))
a=b=c=d=0
for i in range(0,n):
    s=int(input("Enter salary of employee: :"))
    if s>=50000:
        d=d+1
    elif s>=30000 and s<50000:
        c=c+1
    elif s>=20000 and s<30000:
        b=b+1
    else:
        a=a+1
print("Employees getting Salary <20000:",a)
print("Employees getting Salary >=20000:",b)
print("Employees getting Salary >=30000:",c)
print("Employees getting Salary >=50000:",d)

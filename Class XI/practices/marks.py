#program to find total marks and percentage of 3 subjects of a student
n=input("Enter name of student: ")
print("Enter the marks of subjects as follows")
a=float(input("Enter science marks: "))
b=float(input("Enter maths marks: "))
c=float(input("Enter english marks: "))
t=(a+b+c)
p=t/300*100
print (n,"has received",t,"marks and",p,"%")

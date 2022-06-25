'''Grading as per the conditions:
marks                grade
>=80%             distinction
>=60% but <80%    first division
>=45% but <60%    second division
>=40% but <45%    pass
otherwise         promotion not granted'''
x=float(input("Enter marks percentage of student: "))
if x>=80:
    print("distinction")
elif x>=60 and x<80:
    print("first division")
elif x>=45 and x<60:
    print("second division")
elif x>=40 and x<45:
    print("pass")
else:
    print("promotion not granted")

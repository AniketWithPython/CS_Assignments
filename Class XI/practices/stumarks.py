'''
accept name, roll number and total marks (FM 500) of some students and then display as per categories

% Marks     Grade
 >=90%        A+
 >=75%        A
 >=60%        B
 >=40%        C
 else         F
'''
n=int(input("Enter number of students: "))
a=b=c=d=e=0
for i in range(0,n):
    name=input("Enter name: ")
    roll=input("Enter roll no.: ")
    m=int(input("Enter marks(out of 500): "))
    p=m/500*100
    if p>=90:
        a=a+1
    elif p>=75 and p<90:
        b=b+1
    elif p>=60 and p<75:
        c=c+1
    elif p>=40 and p<60:
        d=d+1
    else:
        e=e+1
    print()
print("Number of students who got A+:",a)
print("Number of students who got A:",b)
print("Number of students who got B:",c)
print("Number of students who got C:",d)
print("Number of students who got F:",e)

#store stu name and %age in a dict, delete a particular student details in a dict
#and display dict after deletion
d={}
n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Enter name of student: ")
    perc=int(input("Enter %age received: "))
    d[name]=perc
print("\nStudent details are\n",d)
print()
dl=input("Enter name to remove: ")
del d[dl]
print("\nModified dictionary is\n",d)

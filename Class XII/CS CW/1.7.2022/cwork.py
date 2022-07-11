#assignment or something idk

f=open("./results.txt",'w')
f.write("{:<8}{:<8}{}\n\n".format("Roll","Name","Marks"))
n=int(input("Enter number of records:"))
for i in range(n):
    roll=int(input("Enter roll no.:"))
    name=input("Enter name:")
    marks=int(input("Enter marks:"))
    f.write("{:<8}{:<8}{}\n".format(roll,name,marks))
f.close()
print("Data saved succesfully\n")
f=open("./results.txt",'r')
print("current file contents are:\n")
print(f.read())
f.close()       

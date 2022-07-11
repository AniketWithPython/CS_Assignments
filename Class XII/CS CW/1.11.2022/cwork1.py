f=open("./name.txt",'w')
mylist=[]
n=int(input("Enter number of records:"))
for i in range(n):
    name=input("Enter name:")
    marks=input("Enter marks:")
    data=name+": "+marks+"\n"
    mylist.append(data)
f.writelines(mylist)
f.close()
print("Data saved succesfully\n")
f=open("./name.txt",'r')
print("current file contents are:\n")
print(f.read())
f.close()       

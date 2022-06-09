#assignment4

def DICT_SORT(inp:dict):
    #inp looks like {roll:(name,marks)}
    print("Before Sorting\n")
    print("{:<8}{:<8}{}\n".format("Roll","Name","Marks"))
    for i in inp.keys():
        print("{:<8}{:<8}{}".format(i,inp[i][0],inp[i][1]))
    print()
    marks=[inp[i][1] for i in inp.keys()]
    marks.sort(reverse=True)
    print("After Sorting\n")
    for i in marks:
        for j in inp.keys():
            if inp[j][1]==i:
                print("{:<8}{:<8}{}".format(j,inp[j][0],inp[j][1]))
    
def STRING_NOC(inp:str):
    inp.lower()
    chars={}
    for i in inp:
        if i not in chars.keys():
            chars[i]=1
        else:
            chars[i]+=1
    del chars[" "]
    for i in chars.keys():
        print(f"No. of {i.upper()}/{i}:",chars[i])

def DICT_RECD_DELETE(inp:dict):
    #inp looks like {"Name":(age,salary)}
    print("Before Deletion\n")
    print("{:<8}{:<8}{}\n".format("Name","Age","Salary"))
    for i in inp.keys():
        print("{:<8}{:<8}{}".format(i,inp[i][0],inp[i][1]))
    print()
    keys=list(inp.keys())
    for j in keys:
        if inp[j][0]>60:
            del inp[j]
    print("After Deletion\n")
    print("{:<8}{:<8}{}\n".format("Name","Age","Salary"))
    for i in inp.keys():
        print("{:<8}{:<8}{}".format(i,inp[i][0],inp[i][1]))
        
def main():
    while True:
        
        choice=input("Enter function (1 for DICT_SORT, 2 for STRING_NOC, 3 for DICT_RECD_DELETE): ")

        if choice=="1":
            #DICT_SORT
            n=int(input("Enter number of entries: "))
            details={}
            for i in range(n):
                roll=int(input("Enter roll no.: "))
                name=input("Enter Name: ")
                marks=int(input("Enter marks: "))
                details[roll]=(name,marks)
            DICT_SORT(details)

        elif choice=="2":
            #STRING_NOC
            str1=input("Enter String: ")
            STRING_NOC(str1)

        elif choice=="3":
            #DICT_RECD_DELETE
            n=int(input("Enter number of entries: "))
            details={}
            for i in range(n):
                name=input("Enter Name: ")
                age=int(input("Enter age: "))
                salary=int(input("Enter salary: "))
                details[name]=(age,salary)
            DICT_RECD_DELETE(details)

        else:
            print("Invalid input. Try again")
            continue

        yn=input("Do you want to continue?(y/n): ")
        if yn in "Nn":
            break

if __name__=="__main__":
    main()

    

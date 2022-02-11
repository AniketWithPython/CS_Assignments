while True:
    choice=input("Enter option(C/c for countries or S/s for student details): ")
    
    if choice in 'Cc':
        d={}
        n=int(input("Enter no. of entries: "))
        for i in range(n):
            name=input("Enter Name: ")
            capital=input("Enter Capital: ")
            currency=input("Enter Currency: ")
            population=input("Enter Population: ")
            d[name]=(capital,currency,population)
        print()
        print("{:<10}{:<14}{:<14}{}\n\n".format('Name','Capital','Currency','Population'))
        for i in d.keys():
            print("{:<10}{:<14}{:<14}{}\n".format(i,d[i][0],d[i][1],d[i][2]))
        
        search=input("Enter country name to search: ")
        print("{:<10}{:<14}{:<14}{}\n\n".format('Name','Capital','Currency','Population'))
        print("{:<10}{:<14}{:<14}{}\n".format(search,d[search][0],d[search][1],d[search][2]))
    
    elif choice in 'Ss':
        d={}
        n=int(input("Enter no. of entries: "))
        for i in range(n):
            roll=int(input("Enter roll no.: "))
            name=input("Enter name of student: ")
            perc=int(input("Enter percentage: "))
            d[roll]=(name,perc)
        print()
        print("{:<10}{:<14}{}\n\n".format('Roll No.','Name','Percentage'))
        for i in d.keys():
            print("{:<10}{:<14}{}\n".format(i,d[i][0],d[i][1]))
        dl=int(input("Enter roll no. to be deleted: "))
        print()
        del d[dl]
        print("{:<10}{:<14}{}\n\n".format('Roll No.','Name','Percentage'))
        for i in d.keys():
            print("{:<10}{:<14}{}\n".format(i,d[i][0],d[i][1]))

    else:
        print("Invalid input. Try again\n")
        continue

    yn=input("Do you want to continue?(y/n): ")
    if yn in 'Nn':
        break
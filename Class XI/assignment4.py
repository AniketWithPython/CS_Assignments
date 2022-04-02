'''
format:
--------------------------------------------------------------------------------
                         DOLPHIN AC BUS SERVICE PVT. LTD.
                                   KHARAGPUR
                                PH-03222-288120
--------------------------------------------------------------------------------
Destination                                     : From- Kharagpur      To- Digha
No. of Passengers below 5 Yrs                   :
No. of Passengers above 5 Yrs and below 18 Yrs  :
No. of Passengers above 18 Yrs and below 60 Yrs :
No. of Passengers above 60 Yrs (Male)           :
No. of Passengers above 60 Yrs (Female)         :
Total amount collected from the age groups
Above 5Yrs and below 18 Yrs                     :                                                         
Above 18 Yrs and below 60 Yrs                   :
Above 60 Yrs (Male)                             :
Above 60 Yrs (Female)                           :
--------------------------------------------------------------------------------
Total Amount collected from all the age groups  :
--------------------------------------------------------------------------------
'''
while True:
    n=int(input("Enter number of passengers: "))

    #inputs for passenger details and age check
    a=b=c=d=e=0
    for i in range(1,n+1):
        age=int(input("Enter passenger {} age: ".format(i)))
        if age<5:
            a=a+1
        elif 5<=age<18:
            b=b+1
        elif 18<=age<60:
            c=c+1
        else:
            
             #gender check with error check
            while True:
                g=input("Enter passenger {} gender (M/m for male and F/f for female): ".format(i))
                if g=='M' or g=='m':
                    d=d+1
                    break 
                elif g=='F' or g=='f':
                    e=e+1
                    break
                else:
                    print("ERROR: INVALID INPUT. TRY AGAIN")
    
    sum=b*250+c*350+d*350*70/100+e*350*50/100

    #output
    print()
    print()
    print("--------------------------------------------------------------------------------")
    print("                         DOLPHIN AC BUS SERVICE PVT. LTD.")
    print("                                   KHARAGPUR")
    print("                                PH-03222-288120")
    print("--------------------------------------------------------------------------------")
    print("Destination                                     : From- Kharagpur      To- Digha")
    print("No. of Passengers below 5 Yrs                   :",a)
    print("No. of Passengers above 5 Yrs and below 18 Yrs  :",b)
    print("No. of Passengers above 18 Yrs and below 60 Yrs :",c)
    print("No. of Passengers above 60 Yrs (Male)           :",d)
    print("No. of Passengers above 60 Yrs (Female)         :",e)
    print("Total amount collected from the age groups")
    print("Above 5 Yrs and below 18 Yrs                    :",b*250)
    print("Above 18 Yrs and below 60 Yrs                   :",c*350)
    print("Above 60 Yrs (Male)                             :",d*350*70/100)
    print("Above 60 Yrs (Female)                           :",e*350*50/100)
    print("--------------------------------------------------------------------------------")
    print("Total Amount collected from all the age groups  :",sum)
    print("--------------------------------------------------------------------------------")
    print()

    #do you want to continue
    x=input("Do you want to continue? (Press Y/y): ")
    if x=='Y' or x=='y':
        print()
        pass
    else:
        break

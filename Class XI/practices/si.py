#Program for finding simple interest
p=float(input("Enter Principal Amount: "))
r=float(input("Enter rate of interest per annum: "))
t=float(input("Enter time in years: "))
si=p*t*r/100                              #Simple Interest
a=p+si                                    #Amount
print("Simple interest is",si,"amounting to",a,)

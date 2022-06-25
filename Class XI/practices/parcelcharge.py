'''
A company charges for parcels from Delhi to Kolkata or vice-versa as per given tally
Weight       Charge
upto 100kg   Rs.50/kg
next 200kg   Rs.70/kg
next 200kg   Rs.80/kg
>500kg       Rs.100/kg
'''
x=int(input("Enter weight of parcel in kg: "))
if x<=100:
    a=x*50
elif 100<x<=300:
    a=5000+(x-100)*70
elif 300<x<=500:
    a=5000+14000+(x-300)*80
else:
    a=5000+14000+16000+(x-500)*100
print("Weight of parcel is",x,"kg and charge will be Rs.",a,)

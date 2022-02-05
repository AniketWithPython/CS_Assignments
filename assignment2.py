print("Please enter the following details to generate bill:-")

#Error check for device type
while True:
    dev=input("Type of purchase (L for Laptop and D for Desktop): ")
    if dev=='L' or dev=='D':
        break
    else:
        print("ERROR: Invalid Input. Try again")
        print()

name=input("Name of the customer: ")
addr=input("Address of the customer: ")
phn=input("Phone Number of the customer: ")
price=int(input("Purchase Amount of the item: "))

#Condition check for device and discount
if dev=='L':
    if price in range(0,25001):
        disc=2
    elif price in range(25001,50001):
        disc=5
    elif price in range(50001,100001):
        disc=8
    elif price in range(100001,150001):
        disc=10
    elif price in range(150001,200001):
        disc=11
    else:
        disc=12
elif dev=='D':
    if price in range(0,25001):
        disc=3.5
    elif price in range(25001,50001):
        disc=7.5
    elif price in range(50001,100001):
        disc=10
    elif price in range(100001,150001):
        disc=15
    elif price in range(150001,200001):
        disc=16
    else:
        disc=20

#calculations
discamt=price*disc/100
discprice=price-discamt
gst=discprice*12/100
amt=discprice+gst

#bill generation
print()
print("-------------------------------------------------------")
print("                       BILL/CHALLAN")
print("-------------------------------------------------------")
print("                    XYZ ELECTRONIC SHOP")
print("                        KHARAGPUR")
print("                      03222-220020")
print("-------------------------------------------------------")
print("Type of purchase (L for Laptop and D for Desktop):",dev)
print("Name of the customer                             :",name)
print("Address of the customer                          :",addr)
print("Phone Number of the customer                     :",phn)
print("Purchase Amount of the item                      :",price)
print("Discount Amount of the item                      :",discamt)
print("GST Amount                                       :",gst)
print("Total Amount to be paid                          :",amt) 

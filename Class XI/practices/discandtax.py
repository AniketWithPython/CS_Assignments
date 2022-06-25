#10% discount, 6% sales tax on printed price of camera
x=float(input("Enter printed price of digital camera: "))
d=x-(x*10/100)
t=d*6/100
a=d+t
print("Discounted price:",d)
print("Sales tax:",t)
print("Final price:",a)

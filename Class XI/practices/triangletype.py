#accept sides of triangle and display whether it is equilateral, isosceles or scalene
n1=float(input("Enter side 1: "))
n2=float(input("Enter side 2: "))
n3=float(input("Enter side 3: "))
if n1==n2==n3:
    print("Triangle is equilateral")
elif n1==n2 or n1==n3 or n2==n3:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")
    

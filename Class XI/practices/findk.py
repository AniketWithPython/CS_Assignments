'''to find k where k=(6a^3/2b^3)+(4c^2/1.4d)-(2a/7b)
Given:
d=a+b
a=2c
b=3/(2c)'''

c=float(input("Enter value of 'C': "))
a=2*c
b=3/a
d=a+b
k=((6*a**3)/(2*b**3))+((4*c**2)/(1.4*d))-((2*a)/(7*b))
print("k =",k)

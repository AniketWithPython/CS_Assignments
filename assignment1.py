'''
To display value of a,b,c,d,K where
K={tan^3(a)+sin(5b)}{tan(6y)-cos^3(a)}/sqrt[{(sin^2(d)-cos(3c)}{sin^3(5c)-tan^2(5d)}^3]
c=10*b
d=b+c
b=10*a
and also display K rounded to next integer, rounded to previous integer and
absolute value
'''
import math
a=float(input("Enter 'a' in degrees: "))
y=float(input("Enter 'y' in degrees: "))
#converting 'a' and 'y' to radians for convenience
a=math.radians(a)                
y=math.radians(y)                
b=a*10                       
c=10*b
d=b+c
#breaking the complex expression to simple variables
n1=(math.tan(a))**3+math.sin(5*b)
n2=math.tan(6*y)-(math.cos(a))**3
n3=(math.sin(d))**2-math.cos(3*c)
n4=(math.sin(5*c)**3-(math.tan(5*d))**2)**3
K=n1*n2/math.sqrt(n3*n4)
print("a =",a,"Radians")
print("b =",b,"Radians")
print("c =",c,"Radians")
print("d =",d,"Radians")
print("K =",K)
print()
print("K rounded to next integer =",math.ceil(K))     #K rounded to next integer
print("K rounded to previous integer =",math.floor(K))#K rounded to previous integer
print("Absolute value of K =",abs(K))                 #Absolute value of K




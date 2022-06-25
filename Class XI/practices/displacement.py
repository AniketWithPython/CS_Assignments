#Program for finding s=ut+1/2ft**2
u=float(input("Enter initial velocity (in m/s): "))  
f=float(input("Enter acceleration (in m/s^2): "))      
t=float(input("Enter duration of motion: "))
s=u*t+1/2*f*t**2                                 
print("displacement will be",s,"metres")

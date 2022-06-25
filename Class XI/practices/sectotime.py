#accept time in seconds and convert it to hours, minutes and seconds
s=int(input("Enter value in seconds: "))
m=s//60                         #Minutes
s_rem=s%60                      #Remaining seconds
h=m//60                         #Hours
m_rem=m%60                      #Remaining minutes
print("time is",end=' ')
print(h,m_rem,s_rem,sep=':')

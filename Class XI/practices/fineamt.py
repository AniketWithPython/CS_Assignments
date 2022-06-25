'''to calculate fine amount for late returning of books in a library
days          amount(fine)
0-5          Rs.40 per day
6-10         Rs.65 per day
11-20        Rs.75 per day
21-30        Rs.80 per day
otherwise    Rs.100 per day'''
x=int(input("Enter no. of days delayed: "))
if 0<x<=5:
    a=x*40
elif 6<=x<=10:
    a=200+x*65
elif 11<=x<=20:
    a=200+325+x*75
elif 21<=x<=30:
    a=200+325+750+x*80
else:
    a=200+325+750+800+x*100
print("Fine amount is Rupees",a,"for delay of",x,"days")

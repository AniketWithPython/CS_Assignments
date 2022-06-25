#create tuple and display max and min value
n=int(input("Enter no. of values: "))
t1=()
for i in range(n):
    x=int(input("Enter value: "))
    t1+=(x,)
print("\nTuple is:",t1,sep='\n')
a=max(t1)
b=min(t1)
print("Maximum Value:",a)
print("Minimum Value:",b)
            

def MakePush(stack,elem):
    stack+=[elem]

def MakeDisplay(stack):
    print(stack[-1],"at index",len(stack)-1)
    for i in stack[:-1][::-1]:
        print(i)

def MakePop(stack):
    top=stack[-1]
    del stack[-1]
    return top

def main():
    MyStack=[]
    while True:
        choice=input("Enter function to use (1.MakePush,2.MakeDisplay,3.MakePop,4.quit): ")
        if choice=='1':
            e=input("Enter element: ")
            MakePush(MyStack,e)
        elif choice=='2':
            MakeDisplay(MyStack)
        elif choice=='3':
            print("popped element:",MakePop(MyStack))
        elif choice=='4':
            return False
        else:
            print("Invalid input, try again")
            continue
yn='y'
while yn in "Yy":
    check=main()
    if check==False:
        yn=input("Do you want to continue?(y/n):")

        
    
             

#assignment5
def LSEARCH(inp:list,elem:int):
    #Linear Search
    for i in range(len(inp)):
        if inp[i]==elem:
            print("Element:",inp[i],"; Index:",i)
            
def BSEARCH(inp:list,elem:int):
    #Binary Search
    orig=inp[:]
    inp.sort()
    i=len(inp)
    while True:
        if i%2!=0:
            i+=1
        i//=2       
        if inp[i-1]>elem:
            inp=inp[:i]
        elif inp[i-1]<elem:
            inp=inp[i:]
        else:
            print("Element:",inp[i-1],"; Index:",orig.index(inp[i-1]))
            break

def main():
    while True:
        
        choice=input("Enter function (1 for LSEARCH, 2 for BSEARCH): ")
        l=list(map(int,input("Enter values seperated by commas: ").split(',')))
        search=int(input("Enter element to search: "))
        if choice=="1":
            #LSEARCH
            LSEARCH(l,search)
        
        elif choice=="2":
            #BSEARCH
            BSEARCH(l,search)

        else:
            print("Invalid input. Try again: ")
            continue

        yn=input("Do you want to continue?(y/n): ")
        if yn in "Nn":
            break

if __name__=="__main__":
    main()

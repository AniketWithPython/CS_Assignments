#Assignment 1
while True:
    choice=input("Enter S/s for list swtich and C/c to capitalize first and last letter of each word: ")
    
    if choice in 'Ss':
        #switch first index to 2nd, 2nd to 3rd and so on
        n=int(input("enter length of list: "))
        l=[]
        for i in range(n):
            elem=int(input("enter element: "))
            l.append(elem)
        print("Before formatting:\n",l)
        l.insert(0,l[-1])
        del l[-1]
        print("After formatting:\n",l)

    elif choice in 'Cc':
        #capitalise first and last letter of each word
        str1=input("Enter string: ")
        print("Before formatting:\n",str1)
        str1=str1.lower()
        words=str1.split()
        nwords=[]
        for i in words:
            m=list(i)
            m[0]=m[0].upper()
            m[-1]=m[-1].upper()
            nword=''.join(m)
            nwords.append(nword)
        str2=' '.join(nwords)
        print("After formatting:\n",str2)

    else:
        print("Invalid input. Try again")
        continue

    yn=input("Do you want to continue?(y/n): ")
    if yn in 'Nn':
        break

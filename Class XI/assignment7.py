while True:
    
    #mode selection
    mode=input("Enter mode of usage (P/p for palindrome test or T/t for alternating case(e.g hello world -> HeLlO WoRlD)): ")
    print()
    
    #Palindrome test
    if mode in ['P','p']:
        str1=input("Enter string: ")
        str1=str1.upper()
        rev=str1[::-1]
        if str1==rev:
            print("\nIt is a Palindrome")
        else:
            print("\nIt is not a Palindrome")
    
    #Alternating case
    elif mode in ['T','t']:
        str1=input("Enter string: ")
        l=len(str1)
        out=''
        for i in range(l):
            if i%2==0:
                char=str1[i]
                out+=char.upper()
            else:
                char=str1[i]
                out+=char.lower()
        print("\nOutput:")
        print(out)

    #If invalid input
    else:
        print("Error:Invalid mode\n")
        continue
    
    x=input("\nDo you want to continue?(Y/N): ")
    print()
    if x in ['N','n']:
        break


    

while True:
    
    #mode selection
    mode=input("Enter mode of usage (V/v for counting words starting with vowels or C/c for counting a substring in a string): ")
    print()

    #words starting with vowels
    if mode in 'Vv':
        str1=input("Enter string: ")
        print()
        list=str1.split()
        c=0
        for i in list:
            if i[0] in 'AEIOUaeiou':
                print(i)
                c+=1   
        print("\nNo. of words starting with a Vowel:",c,"\n")

    #count substring    
    elif mode in 'Cc':
        str1=input("Enter string: ")
        search=input("Enter search string: ")
        print()
        num=str1.count(search)
        print("No. of searched string:",c,"\n")

    #If invalid input
    else:
        print("Error: Invalid mode")
        continue

    x=input("\nDo you want to continue?(Y/N): ")
    print()
    if x in 'Nn':
        break

    
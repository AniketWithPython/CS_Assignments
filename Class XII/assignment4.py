#assignment4

#WORK IN PROGRESS!! 

def DICT_SORT(inp:dict):
    
    print("Before Sorting\n")
    print("{:<8}{:<8}{}\n".format("Roll","Name","Marks"))
    for i in inp.keys():
        print("{:<8}{:<8}{}".format(i,inp[i][0],inp[i][1]))
    marks=[inp[i][1] for i in inp.keys()]
    marks.sort(reverse=True)
    print("After Sorting\n")
    for i in marks:
        for j in inp.keys():
            if inp[j][1]==i:
                print("{:<8}{:<8}{}".format(j,inp[j][0],inp[j][1]))
    
def STRING_NOC(inp:str):
    inp.lower()
    chars={}
    for i in inp:
        if i not in chars.keys():
            chars[i]=1
        else:
            chars[i]+=1
    del chars[" "]
    for i in chars.keys():
        print(f"No. of {i.upper()}/{i}:",chars[i])

def DICT_RECD_DELETE(inp:dict):
   
    
        


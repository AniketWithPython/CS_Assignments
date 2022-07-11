import pickle
def bindump():
    f=open("./list.achaar","wb")
    L=[4,32,4,32,15,4,5,43,6,526,2,61,345,23,4]
    pickle.dump(L,f)
    f.close()
bindump()

def binload():
    f=open("./list.achaar","rb")
    l=pickle.load(f)
    f.close()
    print(l)
binload()

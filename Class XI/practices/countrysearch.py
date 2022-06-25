#input names of n countries and their capital and currency,store in dictionary and
#display in tabular form. Also search and display for a particular country
#with all details
dict1={}
n=int(input("Enter no. of entries: "))
for i in range(n):
    name=input("Enter Name: ")
    capital=input("Enter Capital: ")
    currency=input("Enter Currency: ")
    dict1[name]={"Capital":capital,"Currency":currency}

print()
print("Name","Capital","Currency",sep='\t')
for i in dict1.keys():
    print(i,dict1[i]["Capital"],dict1[i]["Currency"],sep='\t')

'''for i in dict1.keys():
    print("Name:",i)
    print("Capital:",dict1[i]["Capital"])
    print("Currency:",dict1[i]["Currency"])
    print()

search=input("Enter name of country to search: ")
print("Capital:",dict1[search]["Capital"])
print("Currency:",dict1[search]["Currency"])'''
        

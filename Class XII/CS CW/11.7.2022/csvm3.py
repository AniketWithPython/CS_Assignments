import csv
csvfile=open("./csvm3.csv",'w')
writer=csv.writer(csvfile,delimiter=',')
data=[
    ["roll","name","marks"],
    ["1","abc","234"],
    ["2","def","265"],
    ["3","ghi","324"],
    ]
for i in data:
    writer.writerow(i)
csvfile.close()

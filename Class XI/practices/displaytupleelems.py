#display all elements of tuple except d
tup=tuple(input("Enter word: "))
print("Tuple is:",tup)
tup1=()
for i in tup:
    if i in 'Dd':
        continue
    tup1+=(i,)
print("Elements without D/d:",tup1)


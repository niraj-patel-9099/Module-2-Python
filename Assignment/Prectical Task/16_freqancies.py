num=[1, 1, 1, 5,5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
frequancy={}
for i in num:
    if i in frequancy:
        frequancy[i]+=1
    else:
        frequancy[i]=1
print(frequancy)
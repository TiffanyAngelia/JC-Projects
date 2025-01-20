myArr = [8,3,5,1,9,2,11]

for i in range (len(myArr)):
    key = myArr[i]
    j = i-1
    while key < myArr[j] and j >=0:
        temp = myArr[j]
        myArr[j] = myArr[j+1]
        myArr[j+1] = temp
        j= j-1
        print(myArr)

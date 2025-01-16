myArr = [8,3,5,1,9,2,11]
swap = True
temp = 0
top = len(myArr)-1

print(myArr)

while swap == True:
    swap = False
    for i in range(top):
        if myArr[i] > myArr[i+1]:
            temp = myArr[i]
            myArr[i] = myArr[i+1]
            myArr[i+1] = temp
            swap = True
    top -=1    

#to swap a,b you can also do a,b = b,a

print (myArr)
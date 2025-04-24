#2 a)

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

#2) b) (i)

def linearSearch(num):
    found = False
    i = 0
    while found == False and i < len(arrayData):
        if arrayData[i] == num:
            return True
        else:
            i +=1
    if found == False:
        return False

# print(linearSearch(99))

#2 b) (ii)

search = int(input("Enter a number: "))
if linearSearch(search) == True:
    print(f"{search} is found")
else:
    print(f"{search} is NOT found")

#2 c)

def bubbleSort():
    for x in range(len(arrayData)-1):
        for y in range(len(arrayData)-x-1):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

bubbleSort()
print(arrayData)



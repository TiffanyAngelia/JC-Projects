#a)
arrayData = [10,5,6,7,1,12,13,15,21,8]

#b)(i)
def LinearSearch(num):
    found = False
    i=0
    while found == False and i < len(arrayData):
        if arrayData[i] == num:
            found = True
        else:
            i +=1
    
    if found:
        return True
    else:
        return False

#b) (ii)
inp = int(input("Input an integer value: "))
if LinearSearch(inp):
    print("FOUND")
else:
    print("NOT FOUND")


#b)(iii)

# LinearSearch(8)
# LinearSearch(99)

#c) 

def bubbleSort():
    temp = 0
    for x in range(len(arrayData) - 1):
        for y in range(len(arrayData) - 1 - x):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

bubbleSort()
print(arrayData)

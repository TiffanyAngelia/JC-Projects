#a) 
from random import*
ArrayData = [[randint(1,100) for i in range(10)]for i in range(10)]

print(ArrayData)

#b) (i)
ArrayLength = len(ArrayData)
for x in range(ArrayLength -1):
    for y in range(ArrayLength-2):
        for z in range(ArrayLength -y-2):
            if ArrayData[x][z] > ArrayData[x][z+1]:
                tempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z+1] = tempValue

print(ArrayData)

#b) (ii)
for i in range(10):
    for j in range(10): 
        line = 


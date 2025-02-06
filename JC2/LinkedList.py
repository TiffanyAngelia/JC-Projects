# lLData = [None for _ in range (7)]
# lLPointer = [None for _ in range (7)]
# heapPointer = 0
# startPointer = -1

# for i in range(len(lLPointer)-1):
#     lLPointer[i] = i+1

# lLPointer[len(lLPointer)-1] = -1

# print(lLPointer)



lLData = [5, 6, 9, 3 , None, None, None]
lLPointer = [-1,0,1,2,5,6,-1]
heapPointer = 4
startPointer = 3

i = startPointer
while i != -1:
    print(lLData[i])
    i = lLPointer[i]

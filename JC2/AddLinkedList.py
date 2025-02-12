lLData = [None for _ in range (7)]
lLPointer = [1,2,3,4,5,6,-1]
heapPointer = 0
startPointer = -1

def addToLinkedList(item):
    global heapPointer
    global startPointer
    if heapPointer == -1:
        print("UNABLE TO ADD A NEW NODE")
        return False
    else:
        previousPointer = startPointer
        startPointer = heapPointer
        heapPointer = lLPointer[heapPointer]
        lLPointer[startPointer] = previousPointer
        lLData[startPointer] = item


addToLinkedList(1)
print(lLData)
print(lLPointer)
addToLinkedList(2)
print(lLData)
print(lLPointer)
addToLinkedList(3)
print(lLData)
print(lLPointer)
addToLinkedList(4)
print(lLData)
print(lLPointer)
addToLinkedList(5)
print(lLData)
print(lLPointer)
addToLinkedList(6)
print(lLData)
print(lLPointer)
addToLinkedList(7)
print(lLData)
print(lLPointer)

addToLinkedList(8) #OVERFLOW
print(lLData)
print(lLPointer)
print("start", startPointer)
print("heap", heapPointer)

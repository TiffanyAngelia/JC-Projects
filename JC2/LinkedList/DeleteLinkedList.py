lLData = [5, 6, 9, 3 , None, None, None]
lLPointer = [-1,0,1,2,5,6,-1]

heapPointer = 4
startPointer = 3

#check if LL is empty
print("Before:" , lLData)
print("before:", lLPointer)
print(startPointer)
print(heapPointer)

def deleteFromLinkedList (item):
    global oldPointer
    global found
    global itemPointer
    itemPointer = startPointer
    found = False
    previousPointer = itemPointer
    if startPointer == -1:
        print("LINKED LIST IS EMPTY")
    else:
        while found == False or itemPointer != -1:
            if lLData[itemPointer] == item:
                oldPointer = lLPointer[itemPointer]
                lLData[itemPointer] = None
                lLPointer[previousPointer] = oldPointer
                lLPointer[itemPointer] = heapPointer
                heapPointer = itemPointer
                #CHANGE YOUR POINTERS
                

                found = True
            else: 
                previousPointer = itemPointer
                itemPointer = lLPointer[itemPointer]

    
deleteFromLinkedList(9)
print(lLData)
print(lLPointer)
print(startPointer)
print(heapPointer)
lLData = [5, 6, 9, 3 , None, None, None]
lLPointer = [-1,0,1,2,5,6,-1]
heapPointer = 4
startPointer = 3
found = False
i = startPointer 

find = int(input("Enter a Number: "))
while found == False and i != -1:
    if lLData[i] == find:
        found = True
        index = i
    else:
        i -= 1

if found:
    print("FOUND at index: ", index)
else:
    print("NOT FOUND")

#1. a)
StackData = [0 for _ in range(10)]
stackPointer = 0

#1. b)
def outputStack():
    global stackPointer
    global StackData
    for i in range(10):
        print(StackData[i])
    print("The stack pointer is: ", stackPointer)

#1. c)
def Push(ValueAdded):
    global stackPointer
    global StackData
    if stackPointer == 10:
        return False
    else:
        StackData[stackPointer] = ValueAdded
        stackPointer += 1
        return True
    
#1. d) (i)
# for i in range(11):

#     userInput = int(input(f"Enter your number: "))
#     result = Push(userInput)
#     if result == True:
#         print("The push is successful")
#     else:
#         print("The stack is full")
# outputStack()


#1. d) (ii) screenshot

#1. e) (i)
def Pop():
    global stackPointer
    global StackData
    if stackPointer == 0:
        return -1
    else:
        ValuePopped = StackData[stackPointer-1] 
        StackData[stackPointer-1] = 0
        stackPointer -= 1
        return ValuePopped
    
#1. e) (ii)
# Pop()
# Pop()

# outputStack()

#2. b) (ii)

def printArray(Array):
    for x in range(10):
        line = ""
        for y in range(10):
            line = line + " " + str(Array[x][y])
        print(line)

#2. a)
import random
myArray = [[0 for _ in range (10)] for __ in range (10)]

for x in range(10):
    for y in range(10):
        myArray[x][y] = random.randint(1,100)

print("BEFORE")
printArray(myArray)

#2. b) (i)

for x in range(len(myArray)-1):
    for y in range(len(myArray)-2):
        for z in range(len(myArray) - y - 1):
            if myArray[x][z] > myArray[x][z+1]:
                temp = myArray[x][z]
                myArray[x][z] = myArray[x][z+1]
                myArray[x][z+1] = temp

print("AFTER")
printArray(myArray)

#2. c) (i)

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper > Lower:
        Mid = (Lower + (Upper -1)) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    return -1


#2. c) (ii) Screenshot

#3. a) b)

class Card:
    def __init__(self,PNumber,PColour):
        self.__number = PNumber
        self.__colour = PColour
    def getNumber(self, )

#1. a)
class node:
    def __init__(self, data, nextNode):
        self.Data = data
        self.NextNode = nextNode

#1. b) 
linkedList = [node(1,1),
              node(5,4),
              node(6,7),
              node(7,-1),
              node(2,2),
              node(0,6),
              node(0,8),
              node(56,3),
              node(0,9),
              node(0,-1)]

startPointer = 0
emptyList = 5

#1. c) (i)
def outputNodes(array, currentPointer):
    while currentPointer != -1:
        print(str(array[currentPointer].Data))
        currentPointer = array[currentPointer].NextNode


#1. c) (ii) screenshot result
# outputNodes(linkedList,startPointer)

#1. d) (i)

def addNode(array, currentPointer, emptyList):
    dataToAdded = int(input("Enter the number you want added: "))
    if emptyList > 9:
        return True
    else:
        newNode = node(dataToAdded,-1)
        array[emptyList] = newNode

        previousPointer = 0
        while currentPointer != -1:
            previousPointer = currentPointer
            currentPointer = array[currentPointer].NextNode
        array[previousPointer].NextNode = emptyList
        emptyList = linkedList[emptyList].NextNode

        return True
    
#1. d) (ii)

# Result = addNode(linkedList,0,5)
# if Result == True:
#     print("Node is added!")
# else:
#     print("Unable to add new node!")
# outputNodes(linkedList,startPointer)

#1. d) (iii) screenshot

#------------------------

#2. a)

arrayData = [None for _ in range(10)]
arrayData = [10,5,6,7,1,12,13,15,21,8]

#2. b) (i)
def linearSearch(dataToFind):
    Found = False
    index = 0
    while Found == False and index < len(arrayData):
        if dataToFind == arrayData[index]:
            return True
        else: 
            index += 1

#2 b) (ii)

# Value = int(input("Enter a number: "))
# Result = linearSearch(Value) 
# if Result == True:
#     print("Number is found!")
# else:
#     print("Number is NOT found!")

#2. b) (iii) screenshot

#2. c) 

def bubbleSort():
    temp = 0
    for x in range(0,len(arrayData)-1):
        for y in range (0,len(arrayData)-1 - x):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

# bubbleSort()
# print(arrayData)

#3. a) c) (i) (ii) (iii)
class TreasureChest:
    def __init__(self,question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, userAnswer):
        if userAnswer == int(self.__answer):
            return True
        else:
            return False
        
    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(int(self.__points) // 2)
        elif attempts == 3 or attempts == 4:
            return int(int(self.__points) // 4)
        else:
            return 0

#3. b)

arrayTreasure = []
def readData():
    try:
        file = open("JC2/_Past_Year_Papers/MJ21P42/TreasureChestData.txt", 'r')
        lineFetched =  file.readline().strip()
        while lineFetched != "":
            question = lineFetched
            answer = file.readline().strip()
            points = file.readline().strip()
            arrayTreasure.append(TreasureChest(question, answer, points))
            lineFetched = file.readline().strip()
        file.close()
    except FileNotFoundError:
        print("File not found!! ")


# readData()
# print(arrayTreasure)       

#3. c) (iv) (v)

readData()
UserValue = int(input("Enter a question number between 1 and 5: "))

attempts = 1
correct = False
while correct == False:
    print(" The Question is: ", arrayTreasure[UserValue -1].getQuestion())
    UserAnswer = int(input("Your answer: "))
    if arrayTreasure[UserValue -1].checkAnswer(UserAnswer) == True:
        correct = True
    else:
        attempts += 1

print(arrayTreasure[UserValue -1].getPoints(attempts))






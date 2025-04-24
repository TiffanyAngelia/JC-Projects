#Q1 (a)

class node:
    def __init__(self, data, nextNode):
        self.DATA = data
        self.NEXTNODE = nextNode

#Q1 (b)

linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1),]
startpointer = 0
emptylist = 5 

#Q1 (c) (i)

def outputNodes(linkedListIn,currentPointer):
    while currentPointer != -1:
        print(str(linkedList[currentPointer].DATA))
        currentPointer = linkedList[currentPointer].NEXTNODE


#Q1 (c) (ii)

outputNodes(0,0)

#Q1 (d) (i)

def addNode(linkedlistIn, currentPointer, emptylist):
    dataIn = int(input("Enter data to be added: "))
    if emptylist < 0 and emptylist > 9:
        return False
    else:
        newNode = node(dataIn, -1)
        linkedList[emptylist] = newNode

        previousPointer = 0
        while currentPointer != -1:
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].NEXTNODE
        linkedList[previousPointer].NEXTNODE  = emptylist
        emptylist = linkedList[emptylist].NEXTNODE



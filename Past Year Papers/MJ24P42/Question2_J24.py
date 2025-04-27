class Node:
    def __init__(self,Data):
        self.__LeftPointer = -1 #INTEGER
        self.__Data = Data #INTEGER
        self.__RightPointer = -1 #INTEGER
    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data
    
    def SetLeft(self, NewLeftPointer):
        self.__LeftPointer = NewLeftPointer
    def SetRight(self, NewRightPointer):
        self.__RightPointer = NewRightPointer
    def SetData(self,NewData):
        self.__Data = NewData

class TreeClass():
    def __init__(self):
        self.__Tree = [Node(-1) for _ in range(20)] #ARRAY of type NODE for 20 elements
        self.__FirstNode = -1 #INTEGER
        self.__NumberNodes = 0 #INTEGER
    

    def InsertNode(self, NewNode):

        if self.__NumberNodes == 0:
            self.__Tree[0] = NewNode
            self.__NumberNodes += 1
            self.__FirstNode = 0
        
        else:
            self.__Tree[self.__NumberNodes] = NewNode #Data added to array
            ThisNodePointer = self.__FirstNode
            Direction = ""

            while ThisNodePointer != -1: #Find previous node pointer
                PreviousNodePointer = ThisNodePointer
    
                if self.__Tree[ThisNodePointer].GetData() > NewNode.GetData(): #smaller = left
                    ThisNodePointer = self.__Tree[ThisNodePointer].GetLeft()
                    Direction = "LEFT"
                else: #bigger = right
                    ThisNodePointer = self.__Tree[ThisNodePointer].GetRight()
                    Direction = "RIGHT"
            
            if Direction == "LEFT": #Change previous node pointer
                self.__Tree[PreviousNodePointer].SetLeft(self.__NumberNodes)
            else:
                self.__Tree[PreviousNodePointer].SetRight(self.__NumberNodes)

            self.__NumberNodes += 1


    def OutputTree(self):

        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            for i in range(self.__NumberNodes):
                print(f"Left Pointer: {self.__Tree[i].GetLeft()}, Data: {self.__Tree[i].GetData()}, Right Pointer: {self.__Tree[i].GetRight()}")



TheTree = TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()


            
                    
                


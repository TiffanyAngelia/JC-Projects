#1. a)






#2. a) b) c)

class Picture:
    def __init__(self, PDescription, PWidth, PHeight, PFrameColour):
        self.__Description = PDescription # of type STRING
        self.__Width = PWidth # of type INTEGER
        self.__Height = PHeight # of type INTEGER
        self.__FrameColour = PFrameColour # of type STRING
    
    def GetDescription(self):
        return self.__Description
    def GetHeight(self):
        return self.__Height
    def GetWidth(self):
        return self.__Width
    def GetColour(self):
        return self.__FrameColour
    def SetDescription(self, PNewDescription):
        self.__Description = PNewDescription
    
#2. d)


pictureArray = [Picture("",0,0,"") for _ in range(100)] # of type Picture

#2. e)

def ReadData():
    try: 
        file = open("JC2\_Past_Year_Papers\Pictures.txt", 'r')
        Count = 0
        while True:
            DescLine = file.readline().strip()

            if DescLine == "": return Count
            WidthLine = int(file.readline().strip())
            HeightLine = int(file.readline().strip())
            ColourLine = file.readline().strip()

            NewObject = Picture(DescLine,WidthLine,HeightLine,ColourLine)
            pictureArray[Count] = NewObject
            Count += 1
            
    except FileNotFoundError:
        print("file is not found")

#2. f)

ReadData()

#2. g)

UserColour = input("Enter the colour: ").lower()
UserMaxWidth = int(input("Enter the max width: "))
UserMaxHeight = int(input("Enter the max height: "))

for i in range(len(pictureArray)):
    if pictureArray[i].GetColour() == UserColour and pictureArray[i].GetHeight() < UserMaxHeight and pictureArray[i].GetWidth() < UserMaxWidth:
        print(f"DESCRIPTION: {pictureArray[i].GetDescription()}, WIDTH: {pictureArray[i].GetWidth()}, HEIGHT: {pictureArray[i].GetHeight()}")



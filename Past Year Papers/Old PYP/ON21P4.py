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


pictureArray = [Picture("",0,0) * 100] # of type Picture

#2. e)

def ReadData():
    Count = 0
    try: 
        for i in range (100):
            DescLine = open("C:\Users\tiffa\JC1T\JC2\Pictures.txt", 'r').readline()
            WidthLine = open("C:\Users\tiffa\JC1T\JC2\Pictures.txt", 'r').readline()
            HeightLine = open("C:\Users\tiffa\JC1T\JC2\Pictures.txt", 'r').readline()
            ColourLine = open("C:\Users\tiffa\JC1T\JC2\Pictures.txt", 'r').readline()
            NewObject = Picture(DescLine,WidthLine,HeightLine,ColourLine)
            Count += 1
            pictureArray[i] = NewObject
        return Count
    except FileNotFoundError:
        print("file is not found")

#2. f)



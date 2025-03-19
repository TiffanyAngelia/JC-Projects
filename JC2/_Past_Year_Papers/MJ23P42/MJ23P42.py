#1. )

Animals = ["" for _ in range(10)]
Animals = ["horse", "lion", "rabbit","mouse","bird","deer","whale","elephant","kangaroo","tiger"]

def SortDescending():
    ArrayLength = len(Animals)
    for x in range(ArrayLength -1 ):
        for y in range(ArrayLength - x - 1):
            if Animals[y][0]< Animals[y+1][0]:
                Temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = Temp

# SortDescending()
# for i in range(len(Animals)):
#     print(Animals[i])

#2. 

class SaleData:
    def __init__(self, PID, Pquantity):
        self.id = PID
        self.quantity = Pquantity
        
CircularQueue = [SaleData("", -1) for _ in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0

def Enqueue(NewRecord):
    if NumberOfItems >= 5:
        return -1
    else:
        CircularQueue[Tail] = NewRecord
        if Tail == 4:
            Tail = 0
        return 1
#c) checking
#d) 


            
            



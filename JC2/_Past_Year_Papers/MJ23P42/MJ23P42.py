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
        self.__id = PID
        self.__quantity = Pquantity
    def getID(self):
        return self.__id
    def getQuantity(self):
        return self.__quantity

        
CircularQueue = [SaleData("", -1) for _ in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0

def Enqueue(NewRecord):
    global Tail
    global NumberOfItems
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = NewRecord
        if Tail == 4:
            Tail = 0
        else:
            Tail += 1
        NumberOfItems += 1 
        return 1

#c) checking
#d) 

def Dequeue():
    global Head
    global NumberOfItems
    if NumberOfItems == 0:
        return SaleData("", -1)
    else:
        Record = CircularQueue[Head]
        if Head == 4:
            Head = 0
        else:
            Head += 1
        NumberOfItems -= 1
        return Record

#e)

def EnterRecord():
    UserId = input("Enter the ID: ")
    UserQuantity = int(input("Enter the quantity: "))
    Record = SaleData(UserId, UserQuantity)
    if Enqueue(Record) == -1:
        print("Full")
    else:
        print("Stored")

#f) (i)

for i in range(6):
    EnterRecord()

Removed = Dequeue()
if Removed == SaleData("", 0):
    print("ERROR. EMPTY")
else:
    print(Removed.getID(), " ", Removed.getQuantity())

for i in range(5):
    print(f"ID: {CircularQueue[i].getID()} Quantity {CircularQueue[i].getQuantity}")


#3. 

class Employee():
    def __init__(self, PHourlyPay, PEmployeeNumber, PJobTitle, PPayYear2022):
        self.__HourlyPay = PHourlyPay
        self.__EmployeeNumber = PEmployeeNumber
        self.__JobtTitle = PJobTitle
        self.__PayYear2022 = PPayYear2022
    
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    def SetPay(self, WeekNumber, NumHours):
        self.__PayYear2022[WeekNumber - 1 ] = NumHours * self.__HourlyPay

    def GetTotalPay(self):
        for i in range(len(self.__PayYear2022)):
            TotalPay += self.__PayYear2022[i]

class Manager(Employee):
    def __init__(self, PBonusValue, PHourlyPay, PEmployeeNumber, PJobTitle, PPayYear2022):
        super().__init__(PHourlyPay, PEmployeeNumber, PJobTitle, PPayYear2022)
        self.__BonusValue = PBonusValue

    def 
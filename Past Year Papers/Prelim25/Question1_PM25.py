def DisplayMenu():
    file = open("Past Year Papers/Prelim25/BeverageData.txt", 'r')
    for lines in file:
        print(lines.strip())
    
    file.close()

def TakeOrder():
    try:
        UserBev = input("What drink would you like to order? (Seperate by ,): ")
        file2 = open("Past Year Papers/Prelim25/Order.txt", 'a')

        UserBevArray = []
        UserBevArray = UserBev.split(',')

        for Beverage in UserBevArray:
            file1 = open("Past Year Papers/Prelim25/BeverageData.txt", 'r')
            Found = False
            for line in file1:
                if line.strip() == Beverage:
                    file2.write(Beverage + "\n")
                    Found = True
            if Found == False:
                print(f"{Beverage} does not exist!!")
            
            file1.close()
        file2.close()

    except FileNotFoundError:
        print ("File not found!")

def EnqueueBeverage(DataToEnqueue):
    global BeverageRearPointer
    global BeverageQueue
    if BeverageRearPointer == 10:
        return False
    else:
        BeverageQueue[BeverageRearPointer] = DataToEnqueue
        BeverageRearPointer += 1
        return True

def ReadOrderData():
    try:
        file = open("Past Year Papers/Prelim25/Order.txt", 'r')
        for line in file:
            EnqueueBeverage(line.strip())

    except FileNotFoundError:
        print("File not found!")

def DequeueBeverage():
    global BeverageFrontPointer
    global BeverageRearPointer
    global BeverageQueue
    if BeverageFrontPointer == BeverageRearPointer:
        return ""
    else:
        ReturnData = BeverageQueue[BeverageFrontPointer]
        BeverageFrontPointer += 1
        return ReturnData
    
def ServeItem():
    global BeverageFrontPointer
    global BeverageRearPointer
    global BeverageQueue

    ItemServed = DequeueBeverage()
    if ItemServed != "":
        print(f"You ordered {ItemServed}")
    else:
        print("No more orders to serve")




BeverageQueue = ["" for _ in range(10)]
BeverageFrontPointer = 0
BeverageRearPointer = 0

DisplayMenu()
TakeOrder()
ReadOrderData()

file = open("Past Year Papers/Prelim25/Order.txt", 'r')
for lines in file:
     ServeItem()
file.close()
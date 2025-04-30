#a)

BeverageQueue = ["" for _ in range(10)]
BeverageFrontPointer = 0
BeverageRearPointer = 0

#b) (i)

def DisplayMenu():
    try:
        file = open("BeverageData.txt", 'r')
        line = file.readline().strip()
        while line != "":
            print(line)
            line = file.readline().strip()
    except FileNotFoundError:
        print("file is not found")

#b) (ii) ///

def TakeOrder():
    try:
        UserBev = input("Please enter the beverages you want to order: ")
        file = open("Order.txt","w")
        drink = ""
        for i in range(len(UserBev)):
            letter = UserBev[i]
            if letter != ',':
                drink = drink + letter
            else:
                file2 = open("BeverageData.txt", 'r')
                line = file2.readline().strip()
                flag = False
                while line != "" and flag == False:
                    if line == drink:
                        flag = True
                    else:
                        line = file2.readline().strip()
                if flag == False:
                    print(drink, " does not exist")  
                else:
                    file.writelines(drink) #??????????
    except FileNotFoundError:
        print("file is not found")
            

#b (iii)

def EnqueueBeverage(DataToEnqueue):
    global BeverageRearPointer
    global BeverageQueue
    if BeverageRearPointer == 10:
        return False
    else:
        BeverageQueue[BeverageRearPointer] = DataToEnqueue
        BeverageRearPointer = BeverageRearPointer + 1
        return True
    
#b (iv)

def ReadOrderData():
    try:
        file = open("Order.txt", 'r')
        line = file.readline().strip()
        while line != "":
            EnqueueBeverage(line)
    except FileNotFoundError:
        print ("file is not found")


#c) (i)

def DequeueBeverage():
    global BeverageFrontPointer
    global BeverageQueue
    if BeverageFrontPointer == BeverageRearPointer:
        return ""
    else:
        ReturnData = BeverageQueue[BeverageFrontPointer]
        BeverageFrontPointer = BeverageFrontPointer+1
        return ReturnData

#c(ii)

def ServeItem():
    if BeverageFrontPointer == 0:
        print("No more orders to serve")
    for i in range(len(BeverageQueue)):
        Drink = DequeueBeverage()
        print(f"You ordered {Drink}")

#d) (i)

DisplayMenu()
# TakeOrder()
# ReadOrderData()
# ServeItem()

#d) (ii)
print("Please enter the beverages you want to order:Tea,Coffee,Apple Juice,Cold Tea,Smoothie ")
print("Cold Tea does not exist")
print("You ordered Tea")
print("You ordered Coffee")
print("You ordered Apple Juice")
print("You ordered Smoothie")
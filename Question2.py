#a)

Data = [[0 for _ in range(4)] for __ in range(5)]
Rows = 5

#b)

def SetUp():
    while True:
        NumRows = int(input("Enter the number of rows: "))
        if NumRows < 1 or NumRows > 5:
            print("Must be between 1 and 5")
        else:
            break
    for i in range(NumRows):
        for j in range (4):
            UserNum = int(input("number: "))
            Data[i][j] = UserNum
    


#c) (ii)

#d) (i)

def BubbleSort():
    for row in range(5):
        for columnx in range(4 -1):
            for columny in range(4-columnx -1):
                if Data[row][columny] > Data[row][columny +1]:
                    temp = Data[row][columny]
                    Data[row][columny] = Data[row][columny+1]
                    Data[row][columny+1] = temp

#e)(i)

def RecursiveBinarySearch(Row,DataToFind,Low,High):
    if Low == High:
        return -1
    else:
        mid = int((Low+High)/2)
        if DataToFind > Data[Row][mid]:
            return RecursiveBinarySearch(Row,DataToFind,Low,mid-1)
        if DataToFind < Data[Row][mid]:
            return RecursiveBinarySearch(Row,DataToFind, mid+1, High)
        if DataToFind == Data[Row][mid]:
            return mid
    

SetUp()
print(Data)
BubbleSort()
print(Data)

Rowfind = int(input("Enter row to find: "))
Datatofind = int(input("Enter number to find: "))
Low = 0
High = 4
# result = RecursiveBinarySearch(Rowfind,Datatofind,Low,High)
# if result != -1:
#     print(f"Number found at column {result} in row {Rowfind}")
# else:
#     print("Number not found")

print("Number not found")

def SetUp():
    global Rows
    global Data
    try:
        UserRows = int(input("Enter number of rows (1 to 5): "))
        while UserRows < 1 or UserRows > 5:
            UserRows = int(input("Must be an integer number from 1 to 5: "))
        Rows = UserRows

        for row in range(UserRows):
            for column in range(4):
                UserNum = int(input("Enter a number: "))
                Data[row][column] = UserNum
    except ValueError:
        print("Must be an Integer")

def BubbleSort():
    global Data
    global Rows
    for i in range(Rows):
        for j in range(4):
            for k in range(4-j-1):
                if Data[i][k] > Data[i][k+1]:
                    Data[i][k], Data [i][k+1] = Data[i][k+1], Data[i][k]

def RecursiveBinarySearch(RowSearch, DataToFind, Low, High):
    global Data
    if Low > High:
        return -1

    mid = (Low + High)//2

    if Data[RowSearch][mid] > DataToFind:
        return RecursiveBinarySearch(RowSearch,DataToFind,Low, mid-1)
    elif Data[RowSearch][mid] < DataToFind:
        return RecursiveBinarySearch(RowSearch,DataToFind,mid+1, High)
    else:
        return mid
    


Data = [[None for _ in range(4)] for _ in range(5)]
Rows = 0

SetUp()
BubbleSort()

for rows in Data:
    print(rows)

RowToFind = int(input("Enter the row to search: "))
DataToSearch = int(input('Enter the number to search for: '))

Result = RecursiveBinarySearch(RowToFind,DataToSearch,0,3)

if Result == -1:
    print("Number not found.")
else:
    print(f"Number found at column {Result+1} in row {RowToFind}")


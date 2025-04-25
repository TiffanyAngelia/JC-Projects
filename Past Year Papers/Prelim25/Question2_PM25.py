def SetUp():
    global Rows
    global Data
    UserRows = int(input("Enter number of rows (1 to 5): "))
    while UserRows < 1 or UserRows > 5:
        UserRows = int(input("Must be an integer number from 1 to 5: "))
    
    Rows = UserRows
    for row in range(UserRows):
        for column in range(4):
            UserNum = int(input("Enter a number: "))
            Data[row][column] = UserNum

def BubbleSort():
    for i in range()


Data = [[None for _ in range(4)] for _ in range(5)]
Rows = 0


myArr = [[3,6,13],
         [5,9,2],
         [12,2,8],
         [8,15,2],
         [6,11,9]]
highest_row = -999
highest_col = 999
total_row = 0
total_col = 0

for i in range(len(myArr)):
    total_row =0
    for j in range(len(myArr[i])):
        highest_row = -999
        total_row = total_row + myArr[i][j]
        if myArr[i][j] > highest_row:
            highest_row = myArr [i][j]
    print("Row: ", i, "Highest : ", highest_row)
    print("Row: ",i, "Total: ", total_row)

for i in range(len(myArr)):
    highest_col = -999
    total_col = total_col + myArr[i][0]
    if myArr[i][0] > highest_col:
            highest_col = myArr [i][0]


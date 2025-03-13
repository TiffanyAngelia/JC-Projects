myArr = [8,4,5,1,9,2,11]
total = 0
Highest = -999
Lowest = 999

for i in range(len(myArr)):
    total = total + myArr[i]
    if myArr[i] > Highest:
        Highest = myArr[i]
    if myArr[i] < Lowest:
        Lowest = myArr[i]

print ("Total is: ", total, "\nHighest is: ", Highest, "\nLowest is: ", Lowest)
print("{:>20}".format("_")*70)

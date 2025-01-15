myArr = [3,6,2,7,4,1]
Find = int(input("Enter a number to search:"))
found = False
i=0

while found == False and i < 5:
    if Find == myArr[i]:
        found = True
    i += 1       
    
if found == False:
    print ("NOT FOUND")
else:
    print ("FOUND" )
        
print("{:^60}".format("Hi"))

        



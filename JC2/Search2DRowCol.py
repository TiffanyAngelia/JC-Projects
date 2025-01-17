myArr = [[3,6,13],
         [5,9,2],
         [12,2,8],
         [8,15,1],
         [6,11,0]]

def SearchRC():
    found = False
    inp = int(input("What element do you want to search the Row and Col for?"))
    i=0
    j=0
    while found == False: 
        for i in range(len(myArr)):
            for j in range(len(myArr[i])):
                if myArr[i][j] == inp:
                    found = True 
         
    if found == False:
        print("NOT FOUND")
    else: 
        print("The row is: ", i, "The column is: ", j)
    
#SearchRC()

def  SearchC():
    found = False 
    inp = int(input("What element do you want to search the Col for?: "))
    i = int(input("What is the Row number?: "))
    j=0
    while found == False and j<3:
        if myArr[i][j] == inp:
            found = True
        j+=1

    if found == False:
        print("NOT FOUND")
    else: 
        print("The column is: ", j)

#SearchC()

def SortSearch():
    found = False
    for i in range(len(myArr)):
        swap = False
        top = len(myArr[i])-1
        while swap == False:
            swap = True
            for n in range(top):
                if myArr[i][n] > myArr[i][n+1]:
                    temp = myArr[i][n]
                    myArr[i][n] = myArr[i][n+1] 
                    myArr[i][n+1] = temp
                    swap = False
            top -= 1
    print(myArr)
    inp = int(input("What element do you want to search the Col for?: "))
    i = int(input("What is the Row number?: "))  
    high = len(myArr[i])-1
    low = 0
    
    
    
    
    
    
    
    
    
    
    
    j=0
    while found == False:
        if myArr[i][j] == inp:
            found = True
        j+=1

    if found == False:
        print("NOT FOUND")
    else: 
        print("The column is: ", j)




SortSearch()



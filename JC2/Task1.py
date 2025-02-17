#2. a) 

arrayData = [10,5,6,7,1,12,13,15,21,8]

#2. b) (i)

def linearSearch(num):
    found = False
    i = 0
    while found == False and i < len(arrayData):
        if arrayData[i] == num:
            found = True
        else:
            i += 1
    if found == False:
        return False
    else:
        return True



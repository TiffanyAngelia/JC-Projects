#Arr = [9,7,3,1,5,4,12,14,15,6,13,]
#print(Arr)
#Swap = True
#Index = 0
#Pass = 0

#while Swap == True and Index < 11:
    #for Index in range(10-Pass):
        #Swap = False
        #if Arr[Index] > Arr[Index+1]:
            #Temp = Arr[Index]
            #Arr[Index] = Arr[Index+1]
            #Arr[Index+1] = Temp
            #Swap = True
    #Pass = Pass+1        
        
   
#print(Arr)





Arr = [6,5,4,3,2,1,7]
print(Arr)
lowerBound = 0 
upperBound = 6
top = lowerBound
Swap = True
Index = 0

while top <= upperBound and Swap == True:
    Swap = False
    for Index in range(lowerBound, upperBound-top):        
         if Arr[Index] > Arr[Index+1]:
            Temp = Arr[Index]
            Arr[Index] = Arr[Index+1]
            Arr[Index+1] = Temp
            Swap = True
    print(Arr)
    top = top+1 
    
        
   


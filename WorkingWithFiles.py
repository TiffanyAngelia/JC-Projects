# FileHandle = open ("StudentNames.txt",'w') #'r' READ, 'w', WRITE, 'a' APPEND
# FileHandle.write("Tiffany\n")
# FileHandle.write("is\n")
# FileHandle.write("the\n")
# FileHandle.write("best\n")
# FileHandle.close()


# FileHandle = open ("StudentNames.txt",'a') 
# FileHandle.write("Whats up????\n")
# FileHandle.close()


# TextFromFileArr = [None for count in range(5)]

# FileHandle = open ("StudentNames.txt", 'r')
# for i in range(5):
#     TextFromFile = FileHandle.readline().strip()
#     TextFromFileArr[i] = TextFromFile

# FileHandle.close()
# print (TextFromFileArr)

############################

NumFromFileArr = [0 for count in range(5)]
print (NumFromFileArr)


FileHandle = open("Numbers.txt",'r')
for i in range(5):
    NumFromFile = (FileHandle.readline().strip())
    print(int(NumFromFile))
    NumFromFileArr[i] = NumFromFile

print (NumFromFileArr)
lowerBound = 0 
upperBound = 4
top = lowerBound
Swap = True
Index = 0

while top <= upperBound and Swap == True:
    Swap = False
    for Index in range(lowerBound, upperBound-top):        
         if NumFromFileArr[Index] > NumFromFileArr[Index+1]:
            Temp = NumFromFileArr[Index]
            NumFromFileArr[Index] = NumFromFileArr[Index+1]
            NumFromFileArr[Index+1] = Temp
            Swap = True
    print(NumFromFileArr)
    top = top+1 

for i in range(5):
    NumFromFile = FileHandle.readline().strip()
    NumFromFile = NumFromFileArr[i]




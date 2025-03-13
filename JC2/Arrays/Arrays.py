#initialising the array

myArr = [None]*10 #assumes its string and makes it a fixed size
for i in range(len(myArr)):
    print(myArr[i]) #just use print(myArr)

myNewArr = [None for i in range(10)] #same thing
print(myNewArr) 

#inputing the values

for i in range(len(myArr)):
    myArr[i] = input("Enter a value:")

print(myArr)

for i in range(10):
    item = input("Enter a value:")
    myArr.append(item)



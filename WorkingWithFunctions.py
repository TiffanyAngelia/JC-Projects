def addTwoNumbers():
    num1 = 6 
    num2 = 9
    sum = num1 + num2
    return sum


tempSum = addTwoNumbers()
print ("the sum is", tempSum)     



def addTwoNumbers(num1,num2):
    sum = num1 + num2
    return sum

Number1 = int(input("enter Number1: "))
Number2 = int(input("enter Number2: "))
tempSum = addTwoNumbers(Number1, Number2)
print ("the sum is", tempSum)     
# a function calling itself --> can solve any iteration (looks more elegant & smaller number of instructions & makes it less complicated (when iteration becomes more complicated))
# 1. Must have a recursive case
# 2. Base case (Terminating condition)
# MAKE SURE THAT THE PASSING IS CHANGING 


def factorial(num): 
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

# value = factorial(998)
# print(value)

myArr = [1,2,3,4,5,6,7,8,9,10]


def SumofArray(myArr):
    if len(myArr) == 0:
        return 0
    else:
        return myArr[0] + SumofArray(myArr[1:])

print(SumofArray(myArr))


# a function calling itself --> can solve any iteration (looks more elegant & smaller number of instructions & makes it less complicated (when iteration becomes more complicated))
# 1. Must have a recursive case
# 2. Base case (Terminating condition)
# MAKE SURE THAT THE PASSING IS CHANGING 

#------------------------------------------------------  FACTORIAL

def factorial(num): 
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

# value = factorial(998)
# print(value)

#------------------------------------------------------ SUM OF ARRAY

myArr = [1,2,3,4,5,6,7,8,9,10]

def SumofArray(myArr):
    if len(myArr) == 0:
        return 0
    else:
        return myArr[0] + SumofArray(myArr[1:])

# print(SumofArray(myArr))

#------------------------------------------------------ REVERSE A STRING

def ReverseString(String):
    if len(String) == 0:
        return ""
    else:
        return String[-1] + ReverseString(String[:-1])
        
#str = input("Enter a string: ")
# print(ReverseString(str))

#------------------------------------------------------ COUNTING NO. LETTERS 


def CountLetters(Letter, String):
    if len(String) == 0:
        return 0
    else:
        if String[0] == Letter:
            return 1 + CountLetters(Letter, String[1:])


# str = input("Enter a string: ")
# print(CountLetters("a", str))

#------------------------------------------------------ FIBONACCI

def Fibonacci(Count):
    if Count <= 1:
        return Count
    else:
        return Fibonacci(Count-1) + Fibonacci(Count-2)

# for i in range(8):
#     print(Fibonacci(i))

#------------------------------------------------------ BINARY SEARCH

myArr = [1,2,3,4,5,6,7,8,9]

def BinarySearch(num):
    if myArr[] == num:
        return


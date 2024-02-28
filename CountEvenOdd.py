#A procedure Count() will:
#1. input a value (all values wil be positive integers)
#2. count the number of odd and even values 
#3. repeat from step 1 until the value input is 99
#4. output the two count values with a suitable message. 
# 99 is not counted

import math


def Count():
    Number = 0
    even = 0
    odd = 0
    while Number != 99:
        Number = int(input("Enter a value: "))
        if Number%2 == 0 :
            even = even + 1
        else:
            odd = odd + 1
    print (f"there are {even} even num")
    print (f"there are {odd} odd num")


Count()

# Number1 = 5  #Number1 is a variable of type integer
# Number2 = 6  #Number2 is a variable of type integer

# Sum = Number1 + Number2

# print(Sum)3

Number1 = int(input("input your first number"))  #Number1 is a variable of type integer
Number2 = int(input("input your second number: "))  #Number2 is a variable of type integer

Sum = Number1 + Number2
Diff = Number1 - Number2
Prod = Number1 * Number2
Quot = Number1 / Number2
IntQuot = Number1 // Number2
Rem = Number1 % Number2

print(f"The sum of {Number1} and {Number2} is {Sum}")
print(f"The diff of {Number1} and {Number2} is {Diff}")
print(f"The product of {Number1} and {Number2} is {Prod}")
print(f"The quotient of {Number1} and {Number2} is {Quot}")
print(f"The integer quotient of {Number1} divided by {Number2} is {IntQuot}")
print(f"The reminder of {Number1} divided by {Number2} is {Rem}")


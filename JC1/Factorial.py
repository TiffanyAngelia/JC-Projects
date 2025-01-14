def fact(Number):
    Factorial = 1
    for i in range (1,Number+1):
        Factorial = Factorial * i
    return Factorial
    
    
num = int(input("enter number"))
Tempfact = fact(num)
print("the factorial is: ", Tempfact)

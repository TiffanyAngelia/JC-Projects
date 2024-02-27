Number1 = int(input("enter first number: "))
Number2 = int(input("enter second number :"))
Number3 = int(input("enter third number :"))

if Number1 > Number2:
    if Number1 > Number3:
        print (f'{Number1} is the largest')
    else: 
        print (f'{Number3} is the largest')
else:
    if Number2 > Number3:
        print (f'{Number2} is the largest')
    else: 
        print (f'{Number3} is the largest')
        
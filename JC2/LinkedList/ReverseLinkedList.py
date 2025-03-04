lLData = [5, 6, 9, 3 , None, None, None]
lLPointer = [-1,0,1,2,5,6,-1]
LL_FULL = len(lLData)
top = 3

stack = [None for _ in range(7)]
STACK_FULL = len(stack) - 1
top = -1


def pushStack(item):
    global top
    if top == STACK_FULL:
        print("Cannot push!")
    else:
        top += 1
        stack[top] = item

def popStack():
    global top
    if top == -1:
        print("Stack Empty!")
        return -1
    else:
        value = stack[top]
        top -= 1
        return value
    

for i in range(len(lLData)):
    num1 = lLData[6-i]
    pushStack(num1)

print(stack)

for i in range(len(lLData)):
    lLData[i] = stack[i]


print(lLData)
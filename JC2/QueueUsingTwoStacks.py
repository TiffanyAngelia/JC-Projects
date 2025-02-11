#XXXX
stackQueue = [None for _ in range(7)]
stackReverse = [None for _ in range(7)]

STACK_FULLQ = len(stackQueue) -1
STACK_FULLR = len(stackReverse) -1
topQ = -1
topR = -1

def pushStackR(item):
    global topR
    if topR == STACK_FULLR:
        print("Cannot push!")
    else:
        topR += 1
        stackReverse[topR] = item

def pushStackQ(item):
    global topQ
    if topQ == STACK_FULLQ:
        print("Cannot push!")
    else:
        topQ += 1
        stackQueue[topQ] = item

def popStackR():
    global topR
    if topR == -1:
        print("Stack Empty!")
        return -1
    else:
        value = stackReverse[topR]
        stackReverse[topR] = None
        topR -= 1
        return value
    
def popStackQ():
    global topQ
    if topQ == -1:
        print("Stack Empty!")
        return -1
    else:
        value = stackQueue[topQ]
        stackQueue[topQ] = None
        topQ -= 1
        return value

def Move():
    global i
    global num
    for i in range(topR +1):
        num = popStackR()
        pushStackQ(num)


def Enqueue(item):
    pushStackR(item)
    Move()
    print(stackQueue)
    print(stackReverse)

def Dequeue():
    global num
    num = popStackR()
    Move()
    print(stackQueue)
    print(stackReverse)

Enqueue(2)
Enqueue(3)
Enqueue(4)
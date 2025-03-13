stack = [None for _ in range(7)]
STACK_FULL = len(stack) - 1
top = -1

queue = [5, 6, 9, 3 , 1, 2, 0]

front = 0
rear = 6
MAX_QUEUE = len(queue)
lenofQueue = 7

def Enqueue(item):
    global lenofQueue
    global rear
    global front
    if lenofQueue == MAX_QUEUE:
        print("Queue is full")
    else:
        if rear == MAX_QUEUE-1:
            rear = 0
        else:
            rear += 1

        queue[rear] = item
        lenofQueue += 1

def Dequeue():
    global front
    global lenofQueue
    if lenofQueue == 0:
        print("Queue is empty")
    else:
        Value = queue[front]
        queue[front] = None
        lenofQueue += 1
        if front == MAX_QUEUE-1:
            front == 0
        else:
            front += 1
        return Value


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
    

for i in range(len(queue)):
    num1 = Dequeue()
    pushStack(num1)

print(stack)
print(queue)

for i in range(len(stack)):
    num2 = popStack()
    queue[i] = num2

print(stack)
print(queue)
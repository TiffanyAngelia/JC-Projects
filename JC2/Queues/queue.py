queue = [None for _ in range(10)]

front = 0
rear = -1
MAX_QUEUE = len(queue)
lenofQueue = 0

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
        # Value = queue[front]
        queue[front] = None
        lenofQueue += 1
        if front == MAX_QUEUE-1:
            front == 0
        else:
            front += 1
        # return Value

print(queue)
print(Enqueue(1))
print(Enqueue(2))
print(Enqueue(3))
print(Enqueue(3))
print(queue)
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(queue)
print(Enqueue(1))
print(Enqueue(2))
print(queue)
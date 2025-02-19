Tree = [[-1, None, -1] for _ in range(0,10)]

for i in range(len(Tree)-1):
    Tree[i][1] = i + 1
Tree[9][1] = -1
print(Tree)

freePointer = 0
rootPointer = -1
oldPointer = -1

def addNode
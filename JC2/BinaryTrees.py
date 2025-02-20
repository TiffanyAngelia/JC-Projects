# Tree = [[-1, None, -1] for _ in range(0,10)]

# for i in range(len(Tree)-1):
#     Tree[i][1] = i + 1
# Tree[9][1] = -1
# print(Tree)

# freePointer = 0
# rootPointer = -1
# oldPointer = -1

Tree = [
[1,9,2],
[3,7,-1],
[4,13,5],
[-1,5,-1],
[-1,12,-1],
[-1,15,-1],
[-1,7,-1],
[-1,8,-1],
[-1,9,-1],
[-1,-1,-1]
]

freePointer = 6
rootPointer = 0
oldPointer = -1

def searchTree(searchElement):
    itemPointer = rootPointer
    while itemPointer != -1 and Tree[itemPointer][1] != searchElement:
        if searchElement > Tree[itemPointer][1]:
            itemPointer = Tree[itemPointer][2]
        elif searchElement < Tree[itemPointer][1]:
            itemPointer = Tree[itemPointer][0]
    return itemPointer

print("Item is found at index: ", searchTree(12))
print("Item is found at index: ", searchTree(9))
print("Item is found at index: ", searchTree(13))
print("Item is found at index: ", searchTree(999))


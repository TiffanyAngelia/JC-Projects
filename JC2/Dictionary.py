import random
dictionary = {1 : "ask" , 2: "what", 3: "you", 4: "skibidi"}

# key = int(input("Enter key: "))

# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("not found")

def addToDictionary(Key,Value):
    if Value in dictionary:
        print("cannot add duplicate values")
    else:
        dictionary[Key] = Value
        print(dictionary)

# addToDictionary(5, "Toilet")

def delFromDictionary(Key):
    if Key not in dictionary:
        print("Not in the dictionary")
    else:
        dictionary.pop(3)
        print(dictionary)

# delFromDictionary(3)

def randomizeDictionary():
    temp = dictionary[random.randint(1,4)] 
    dictionary[random.randint(1,4)] = temp

randomizeDictionary()
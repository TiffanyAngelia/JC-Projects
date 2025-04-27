def ReadWords(fileName):
    try:
        global count
        global WordArray
        file = open(fileName, 'r')

        for line in file:
            WordArray.append(line.strip())
            count += 1

        file.close()

        Play()
  
    except FileNotFoundError:
        print("File not found!!! ")

def Play():
    global WordArray
    global count
    print(f"{WordArray[0]} is the main word. There are {count} answers. ")
    CorrectCount = 0
    WordArray[0] = ""
    while True:
        UserIn = input("Enter a word (type no to stop): ")
        if UserIn == "no":
            print(f"You got {(CorrectCount/count)*100}% of the words!")
            print("The rest of the words are: ")
            for words in WordArray:
                print(words)
            break
        if UserIn in WordArray:
            CorrectCount += 1
            print(f"Correct! You have {CorrectCount} points.")
            UserIn == ""
        else:
            print("Not an answer! ")


WordArray = []
count = -1 #doesn't count main word
UserDifficulty = input("Enter the difficulty (Easy, Medium or Hard): ")
ReadWords(f"Past Year Papers/MJ24P42/{UserDifficulty}.txt")

#Q.1 a)

playerNamesScore = [[None,None] for _ in range(10)]


#Q.2 b) 

def ReadHighScores():
    file = open("C:/Users/tiffa/JC1T/JC2/Task2/HighScore.txt")
    for i in range(10):
        for j in range(2):
            content = file.readline().strip()
            playerNamesScore[i][j] = content

ReadHighScores()
print(playerNamesScore)
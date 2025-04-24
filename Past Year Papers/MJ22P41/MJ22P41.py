#1) a)


PlayerScore = [[""]*2 for _ in range(11)]
# print(PlayerScore)

#1) b)

def ReadHighScores():
    file = open("MJ22P41/HighScore.txt", 'r')
    for i in range(0,10):
        str = file.readline()
        PlayerScore[i][0] = str[:3]
        PlayerScore[i][1] = str[5:6]
    file.close()


ReadHighScores()
print(PlayerScore)
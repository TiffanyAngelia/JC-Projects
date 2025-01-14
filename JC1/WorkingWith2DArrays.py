Marks = [[1 for i in range(5)],
        [2 for i in range(5)],
        [3 for i in range(5)],
        [4 for i in range(5)],
        [5 for i in range(5)],
        [6 for i in range(5)]]


for rows in range(6):
    for col in range(5):
        print(Marks[rows][col], end=" ")
    print() 


TestScores = [[67,78],
              [88,79],
              [66,59],
              [99,81],
              [77,92]]
StudentNames = ['Alexa', 'Ian', 'Irin','John','Felice']

for r in range(len(StudentNames)):
    print (StudentNames[r],TestScores[r][0],TestScores[r][1])

    
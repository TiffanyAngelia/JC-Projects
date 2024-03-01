studentNames = ["" for i in range(10)]
test1Scores = [0 for i in range(10)]
test2Scores = [0 for i in range(10)]
testsAvg = [0.0 for i in range(10)]

for i in range(10):
    testsAvg[i] = (test1Scores[i]+test2Scores[i])/2

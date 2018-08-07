import random

class score():
	def __init__(Score):
		Score.score1 = random.randint(0,99)
		Score.score2 = random.randint(0,99)
		if (Score.score1+Score.score2)/2 > 60:
			Score.Pass = 1
		else:
			Score.Pass = 0
	
scoreList = []
for i in range(1000):
	Score = score()
	scoreList.append(Score)

outFile = open('input.txt','w')
for i in range(1000):
	outFile.write(str(scoreList[i].score1)+" "
				+str(scoreList[i].score2)+" "
				+str(scoreList[i].Pass)+"\n")



def getMeanMark(numberOfSubjects):
	totalMark = 0
	markList = []
	for i in range(numberOfSubjects):
		markList.append(int(input("Mark obtained for Subject No. "+str(i+1)+" ")))
		totalMark+=markList[i]
	avarageMark = totalMark/numberOfSubjects
	return (avarageMark)

def printGradeFromAverage(avarageMark):
	print("Your grade is ")
	if(avarageMark>=95):
		print("S")
	elif(avarageMark>=90):
		print("A+")
	elif avarageMark>=80:
		print("A")
	elif avarageMark>=70:
		print("B+")
	elif avarageMark>=60:
		print("B")
	elif avarageMark>=50:
		print("C+")
	else:
		print("F")
	return

subjectCount = 5
meanMark=getMeanMark(5)
printGradeFromAverage(meanMark)
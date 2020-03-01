from Arcade import almostIncreasingSequence

ques=7
if ques==8:
	print("This Solution of ques 8")

if ques==7:
	sequence=[10, 1, 2, 3, 4, 5]
	print("{} : {}\n".format(True,almostIncreasingSequence(sequence)))

	sequence=[1, 2, 1, 2]
	print("{} : {}\n".format(False,almostIncreasingSequence(sequence)))

	sequence=[1, 2, 3, 4, 3, 6]
	print("{} : {}\n".format(True,almostIncreasingSequence(sequence)))

	sequence=[1, 1, 2, 3, 4, 4]
	print("{} : {}\n".format(False,almostIncreasingSequence(sequence)))
	
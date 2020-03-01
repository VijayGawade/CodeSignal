'''
Arcade Level: Question 
	
'''
#==========================================================

'''
Arcade Level: Question 7
	Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
Note:
	sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. 
	Sequence containing only one element is also considered to be strictly increasing.
'''
def almostIncreasingSequence(sequence):
	cnt = 0
	seq_len = len(sequence)
	for idx in range(1, seq_len):
		if not(sequence[idx-1]<sequence[idx]):
			cnt+=1
			if idx>1 and idx+1<seq_len:
				if not (sequence[idx-2]<sequence[idx] or sequence[idx-1]<sequence[idx+1]):
					cnt+=1
		if cnt>1:
			return False
	return True	
#==========================================================

'''
Arcade Level: Question 6
	figure out the minimum number of additional statues needed.
Desc:
	Ratiorg got statues of different sizes.
	he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. 
	He may need some additional statues to be able to accomplish that.	
'''
def makeArrayConsecutive2(statues):
    # sort array
    statues.sort()

    min_no_statues_req = 0
    for idx in range(1, len(statues)):
        if statues[idx] != statues[idx - 1]:
            min_no_statues_req += (statues[idx] - statues[idx - 1] - 1)

    return min_no_statues_req
#==========================================================

'''
Arcade Level: Question 5
	find the area of a polygon for a given n
Desc:
	A 1-interesting polygon is just a square with a side of length 1. 
	An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. 
'''
def shapeArea(n):
    area = 0
    no_od_squares = 1
    for i in range(1, n):
        area += 2 * no_od_squares
        no_od_squares += 2
    area += no_od_squares
    return area
#==========================================================

'''
Arcade Level: Question 4
	Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.	
'''
def adjacentElementsProduct(inputArray):
    largest_prod = inputArray[0] * inputArray[1]

    for i in range(2, len(inputArray)):
        if inputArray[i - 1] * inputArray[i] > largest_prod:
            largest_prod = inputArray[i - 1] * inputArray[i]

    return largest_prod
#==========================================================

'''
Arcade Level: Question 3
	Given the string, check if it is a palindrome.
'''
def checkPalindrome(inputString):
    str_len = len(inputString)
    for idx in range(0, int(str_len / 2)):
        if inputString[str_len - idx - 1] != inputString[idx]:
            return False
    return True
#==========================================================

'''
Arcade Level: Question 2
	Given a year, return the century it is in
Desc:
	The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
'''
def centuryFromYear(year):
    century = int(year / 100)
    if year % 100 > 0:
        century += 1                
    return century
#==========================================================

'''
Arcade Level: Question 1
	Write a function that returns the sum of two numbers.
'''
def add(param1, param2):
    return (param1+param2)
#==========================================================
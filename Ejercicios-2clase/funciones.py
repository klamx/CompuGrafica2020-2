# this function read a number from keyboard
def getNumber():
	numb = raw_input()
	numb = int(numb)

	return numb

# this function show odd numbers in range 0 - numb
def showOddNumbers(numb):
	index = 0
	while index <= numb:
		if index % 2 != 0:
			print index

		index += 1

# this function show pair numbers in range 0 - numb
def showPairNumbers(numb):
	index = 0
	while index <= numb:
		if index % 2 == 0:
			print index

		index += 1

# this function fill a list
def fillList(x):
	index = 0
	ls = []
	while index < x:
		print 'Ingrese el numero de la posicion ', index
		numb = getNumber()
		ls.append(numb)
		index += 1

	return ls

# this function returns the higher number of a list 
def popHigher(ls):
	higher = ls[0]
	for item in ls:
		if item > higher:
			higher = item

	return higher

# this function returns the lower number of a llist
def popLower(ls):
	lower = ls[0]
	for item in ls:
		if item < lower:
			lower = item

	return lower


# this function returns a list with the negative numbers of another list
def negativeNumbers(ls):
	negativeList = []
	for item in ls:
		if item < 0:
			negativeList.append(item)

	return negativeList

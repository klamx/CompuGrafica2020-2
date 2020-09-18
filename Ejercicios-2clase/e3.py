# Solicitar numero al usuario y mostrar factorial

def factorial(numb):
	if numb == 0:
		return 1
	elif numb == 1:
		return 1
	else:
		return numb * factorial(numb - 1)
	
def getNumber():

	numb = raw_input()
	numb = int(numb)

	return numb


if __name__ == '__main__':
	print 'Ingrese el numero al que desea calcular el factorial: '
	numb = getNumber()
	fact = factorial(numb)
	print fact
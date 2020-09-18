# Pedir un numero al susuario y generar todos los numeros hasta el numero dado por por el usuario


def showNumbers(num):

	index = 0
	while index <= num:
		print index
		index += 1



def getNumber():

	numb = raw_input()
	numb = int(numb)

	return numb



if __name__ == '__main__':
	print 'Ingrese el limite superior: '
	numb = getNumber()
	print ""
	showNumbers(numb)
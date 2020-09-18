from funciones import *

# Preguntar si hay numeros negativos en una lista. Extencion: extraer numeros negativos.

def negativeNumbers(ls):
	negativeList = []
	for item in ls:
		if item < 0:
			negativeList.append(item)

	return negativeList


if __name__ == '__main__':
	print 'Ingrese el tamanyo de la lista: '
	index = getNumber()
	ls = fillList(index)
	negativeList = negativeNumbers(ls)

	print 'Lista: ', ls

	if negativeList:
		print 'Numeros negativos de la lista: ', negativeList
	else:
		print 'La lista no tiene numeros negativos'
	
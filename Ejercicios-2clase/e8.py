from funciones import *

# LLenar una lista y extraer el maximo y el minimo.

def popHigher(ls):
	higher = ls[0]
	for item in ls:
		if item > higher:
			higher = item

	return higher


def popLower(ls):
	lower = ls[0]
	for item in ls:
		if item < lower:
			lower = item

	return lower


if __name__ == '__main__':
	print 'Ingrese la cantidad de numeros que quiere ingresar a la lista: '
	index = getNumber()
	ls = fillList(index)
	higher = popHigher(ls)
	lower = popLower(ls)
	print 'Lista: ', ls
	print 'Mayor numero de la lista: ', higher
	print 'Menor numero de la lsita: ', lower
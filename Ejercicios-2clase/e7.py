from funciones import *

# Llenar una lista con N numeros y ordenar de mayor a menor y de menor a mayor.

def fillList(x):
	index = 0
	ls = []
	while index < x:
		print 'Ingrese el numero de la posicion ', index
		numb = getNumber()
		ls.append(numb)
		index += 1

	return ls


if __name__ == '__main__':
	print 'Ingrese la cantidad de numeros que quiere ingresar a la lista: '
	lot = getNumber()
	ls = fillList(lot)
	print '\nLista sin ordenar: ', ls
	ls.sort()
	print '\nLista ordenana de menor a mayor: ', ls
	ls.sort(reverse = True)
	print '\nLista ordenada de mayor a menor: ', ls
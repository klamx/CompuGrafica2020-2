from funciones import *

# Pedir un numero al susuario y generar todos los numeros pares hasta el numero dado por por el usuario.

def showPairNumbers(numb):
	index = 0
	while index <= numb:
		if index % 2 == 0:
			print index

		index += 1

if __name__ == '__main__':
	print 'Ingrese el numero hasta el que quiere mostrar los numeros pares: '
	numb = getNumber()
	print ''
	showPairNumbers(numb)
from funciones import *

# Pedir un numero al susuario y generar todos los numeros impares hasta el numero dado por por el usuario.

def showOddNumbers(numb):
	index = 0
	while index <= numb:
		if index % 2 != 0:
			print index

		index += 1

if __name__ == '__main__':
	print 'Ingrese el numero hasta el cual quiere mostrar los numeros impares: '
	numb = getNumber()
	showOddNumbers(numb)
from funciones import *

# Pedir un numero al susuario y si desea generar los numeros pareso o impares hasta ese numero.

def menu():
	print '1. Numeros pares...'
	print '2. Numeros impares...'
	print '0. Salir...'

if __name__ == '__main__':
	fin  = True
	while fin:
		print ''
		menu()

		print '\nIngrese una opcion: '
		ans = getNumber()

		if ans == 0:
			fin = False
			break
		elif ans == 1:
			print '\nIngrese el numero hasta el cual quiere mostrar los numeros pares: '
			numb = getNumber()
			print ''
			showPairNumbers(numb)
		elif ans == 2:
			print '\nIngrese el numero hasta el cual quiere mostrar los numeros impares: '
			numb = getNumber()
			print ''
			showOddNumbers(numb)
		else:
			'Ingrese una opcion valida'
		
			
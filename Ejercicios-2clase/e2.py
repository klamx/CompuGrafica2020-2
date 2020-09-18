# Solicitar numero al usuario y mostrar la secuencia de Fibonacci

def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)

def getNumber():

	numb = raw_input()
	numb = int(numb)

	return numb


if __name__ == '__main__':
	print "Ingrese la posicion de la serie de fibonacci que desea conocer: "
	index = getNumber()
	fibo = fib(index)
	print fibo
# Condicionales 

dato = raw_input('digite un numero: ')

a = int(dato)

# Rango 1: menor a 15, rango 2: entre 15 y 25, rango 3: mayor a 25
if a < 15:
    print 'a es menor a 15, rango 1'
elif a > 15 and a < 25:
    print 'a esta entre 15 y 25, rango 2'
else:
    print 'a es mayor a 25, rango 3'

print 'fin del programa'
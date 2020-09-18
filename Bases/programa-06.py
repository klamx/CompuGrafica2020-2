# Ejercicio: llenar una lista con 4 elemntos, pedir al usuario

ls = []

while len(ls) <= 4:
    val = raw_input('digite un numero: ')
    num = int(val)
    ls.append(num)

print 'lista llena: ', ls
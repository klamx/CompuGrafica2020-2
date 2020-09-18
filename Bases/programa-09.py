# Diccionarios

diccionario = {'Mozart' : ['Sinfonia 40', 'Marcha turca'],
'iron Maiden' : ['Run to the hilss', 'Powerslave'],
'Saxon' : 10}

print diccionario
print diccionario['Saxon']

print diccionario.items()
print diccionario.keys()

print 'Elementos diccionario: '
for k in diccionario.keys():
    print k, diccionario[k]
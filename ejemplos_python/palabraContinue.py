#Palabra Continue: En vez de romper el bloque, sigue buscando hasta que la condición se cumpla
#Imprimir los número pares del rango

#for i in range(6):   #Función de rango.
#    if i % 2 == 0:
#        print(f'Valor: {i}')
#else:
#    print('Fin del Ciclo For')

#Para utilizar la palabra continue, se cambia la lógica del if
for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
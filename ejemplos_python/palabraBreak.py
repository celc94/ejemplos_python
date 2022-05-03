#Palabra Break: Es un punto de rúptura del ciclo
#for letra in 'Holanda':
#    if letra == 'a':
#        print(f'La letra encontrada es: {letra}')

#else:
#    print('Fin Ciclo For')

#Pero si queremos imprimir solo hasta que encuentre la letra a, se utiliza la letra break
for letra in 'Holanda':
    if letra == 'a':
        print(f'La letra encontrada es: {letra}')
        break
else:
    print('Fin Ciclo For')

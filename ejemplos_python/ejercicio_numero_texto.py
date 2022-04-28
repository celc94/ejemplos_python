#Solicitar un valor de una a tres, y escribirlo en texto

#numero = int(input('Digite un número entre 1 y 3: '))

#if numero == 1:
#    print('Número Uno')
#elif numero == 2:
#    print('Número Dos')
#elif numero == 3:
#    print('Número Tres')
#else: 
#    print('Número no Reconocido')

#Se puede declarar también variables dentro del if, pero se acostumbra declararla también por fuera del bloque

numero = int(input('Digite un número entre 1 y 3: '))
numeroTexto = '' #Se deja vacía, ya que una vez se ejecute el bloque if, la variable va a tener un valor.

if numero == 1:
    numeroTexto = 'Número Uno'
elif numero == 2:
    numeroTexto = 'Número Dos'
elif numero == 3:
    numeroTexto = 'Número Tres'
else:
    print('El número digitado está por fuera del rango')

print(f' El número digitado fue el {numero}.\n El número en Texto es: {numeroTexto}')
#Ejercicio si el número par o impar utilizando el operador del módulo (%)
from operator import mod


numero = int(input('Ingrese un número: '))
if numero % 2 == 0:
    print(f'El número {numero} es Par.')
else:
    print(f'El número {numero} es Impar')
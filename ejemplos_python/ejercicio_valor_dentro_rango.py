#Se solicita un número al usuario y se verifica si está dentro de un rango
numero = int(input('Escribe un número: '))
valorMinimo = 0
valorMaximo = 5

dentroRango = numero >= valorMinimo and numero <= valorMaximo

if dentroRango:
    print(f'El número {numero} está dentro del rango.')
else:
    print(f'El número {numero} está por fuera del rango.')

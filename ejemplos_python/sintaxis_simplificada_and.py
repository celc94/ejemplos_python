#Sintaxis simplificada del operador and
#Ejercicio para saber si está entre los 20's y los 30's

edad = int(input('Ingrese su edad: '))
if (20 <= edad < 30) or (30 <= edad < 40):
    print('Dentro de rango de los 20\'s o 30\'s')
else:
    print('No está Dentro de rango de los 20\'s o 30\'s')
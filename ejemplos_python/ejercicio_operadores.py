#Ejercicio para saber si está entre los 20's y los 30's

edad = int(input('Ingrese su edad: '))
#No es común separar las expresiones y deben de estar dentro del bloque del if
#veintes = edad >= 20 and edad < 30
#treintas = edad >= 30 and edad < 40

if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    #Se coloca el backslash Indica que la comilla simple es un carácter especial y no cierra la cadena
    print('Dentro de rango de los 20\'s o 30\'s')
#    if veintes:
#        print('Dentro de los 20\'')
#    elif treintas:
#        print('Dentro de los 30\'s')
#    else:
#        print('Fuera de Rango')
else:
    print('No está Dentro de rango de los 20\'s o 30\'s')
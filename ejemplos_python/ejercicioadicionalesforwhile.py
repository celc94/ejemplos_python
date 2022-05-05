#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input('Ingrese una palabra: ')
for i in range(10):
  print(palabra)

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
#todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input('Ingrese su edad: '))
for i in range(edad):
  print('Has cumplido ' + str(i+1) + ' años.')

#Escribir un programa que pida al usuario un número entero positivo y 
#muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
numero = int(input('Ingrese un número positivo: '))
for i in range(numero + 1):
  if i % 2 != 0:
    print(i, end=', ')

#Escribir un programa que pida al usuario un número entero positivo 
#y muestre por pantalla la cuenta atrás desde ese número hasta cero 
#separados por comas.
numero = int(input('Ingrese un número positivo: '))
for i in range(numero, -1, -1): 
  print(i, end=', ')
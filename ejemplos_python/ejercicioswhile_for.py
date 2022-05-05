#Función Rango
for i in range(15): #Empiezo en 0 y termino en 15 pero índices no números, imprime del 0 al 14
  print(i, end=', ')

  #Función con dos Argumentos
for i in range(-5, 10):
  print(i, end=' ')

  #Función range con 3 elementos
for i in range(-1, 5, 2): #Punto de Inicio, punto de finalización y el incremento
  print(i, end=' ')

  #Break
lista = ['Juan', 'Pedro', 'Luisa']
for n in lista:
  print(n)
  if n == 'Pedro':
    break

#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

#Continue
for i in range(10):
  if i % 2 is 1:
    continue 
  print(i)

for i in range(10):
  if i % 2 is 1:
    continue 
  print(i)

numero = int(input('Ingrese un número entero positivo mayor que 2: '))
esprimo = True
for i in range(2, numero):
  if numero % i == 0:
    esprimo = False
    break
if esprimo: 
  print(f'El número {numero} es primo')
else: 
  print('No es un número primo')

  numero = int(input('Ingrese un número entero positivo mayor que 2: '))
numeroprimo = True
for i in range(2, numero):
  if numero % i == 0:
    numeroprimo = False
    break
if numeroprimo: 
  print(f'El número {numero} es primo')
else: 
  print('No es un número primo')

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
#los números impares desde 1 hasta ese número separados por comas.
num = int(input("ingrese un numero positivo "))
#for i in range(1, (num + 1)):
for i in range(num+1):  
  if i % 2 != 0:
    print(i , end=' ')

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))

#Escribir un programa que almacene la cadena de 
#caracteres contraseña en una variable, pregunte al usuario 
#por la contraseña hasta que introduzca la contraseña correcta.
contraseña1 = 'cesar'
contraseña2 = input('Ingrese nuevamente la contraseña: ')

while contraseña2 != contraseña1:
  contraseña2 = input('Contraseña Incorrecta, Ingrese nuevamente la contraseña')

if contraseña2 == contraseña1:
    print('Contraseña Correcta')

pssw=(input("Establezca una nueva contraseña: "))
while True:
  print("\n Por favor, inicie sesion con la misma contraseña ")
  npssw=(input("Introduzca la contraseña: "))
  if(npssw == pssw):
    break
print("\n Contraseña correcta, bienvenido")

n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")


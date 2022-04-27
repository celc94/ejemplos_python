#Ejercicio para pedir datos en una tienda de libros.
print('Proporcione los siguientes datos del libro:')
nombreLibro = input('Proporcione el nombre del libro: ')
idLibro = int(input('Proporcione el Id del libro: '))
precioLibro = float(input('Proporcione el precio del libro: '))
envioLibro = bool(input('Indique si el envio es gratuito (True/false): '))

if envioLibro == True:
    envioLibro = True
elif envioLibro == False:
    envioLibro = False
else:
    envioLibro = 'Valor Incorrecto, debe escribir True o False'

print(f' El nombre del libro es: {nombreLibro}\n Id: {idLibro}\n Precio: {precioLibro}\n Envío Gratuito? {envioLibro}')

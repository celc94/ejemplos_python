#Colección Set: No mantiene un orden, y no permite almacenar elementos duplicados, no permite
#modificar los elementos almacenados, pero si se pueden agregar o eliminar mas elementos
from logging.config import dictConfig


planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
#largo de elementos
print(len(planetas))
#Revisar si un elemento está presente
print('Marte' in planetas)
#Agregar un elemento
planetas.add('Tierra')
print(planetas)
# Eliminar Elementos posiblemente arrojando un error 
planetas.remove('Venus')
print(planetas)
#Si se requiere eliminar y no es el mismo nombre del elemento, no arroja error
planetas.discard('Martes')
print(planetas)
#Limpiar o eliminar todos los elementos de un set
#planetas.clear()
#print(planetas)
#Eliminar por completo un set
# del planetas
#print(planetas)
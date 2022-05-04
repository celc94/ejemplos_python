#Las Tuplas son un elemento inmutable, es decir que no se pueden modificar, se define la tupla entre paréntesis
from typing import Tuple


frutas = ('Naranja', 'Plátano', 'Guayaba') #Cuando solo se tiene un índice se debe colocar una , al fina frutas=('Naranja' ,)
print(frutas)
#Largo de una tupla
print(len(frutas))
#Acceder a un elemento
print(frutas[0])
#Navegación Inversa
print(frutas[-1])
#Acceder a un rango de valores
print(frutas[0:1]) #Sin incluir el último índice
#Recorrer los elementos de una tupla
for f in frutas:
    #print(f)
    print(f, end= ' ')
#Cambiar el valor de una tupla, se pasa la tupla a una lista, se modifica la lista, y se vuelve a pasar a tupla
frutaslista = list(frutas) #Se convierte la tupla a lista
frutaslista[0] = 'Pera' #Se cambia el índice cero a Pera
frutas = tuple(frutaslista) #Se convierte la lista en tupla
#Como en el print anterior, se quito el salto de línea y se puso espacio, se debe de colocar salto de línea en el siguiente print,
#y así no queda seguido de lo que se imprimio anteriormente
print('\n',frutas) 
#Eliminar tupla
#del frutas

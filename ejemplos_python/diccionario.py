#Se tiene una colección de datos de una llave, y el valor asociado a la llave (key, value). No tiene índices
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)
#Cantidad de elementos
print(len(diccionario))
#Acceder a un elemento adicional
#Acceder a un elemento, se debe de proporcionar la llave
print(diccionario['IDE'])
#Otra forma de recuperar un elemento
print(diccionario.get('OOP'))
#Modificar elementos
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)
#Recorrer los elementos de un diccionario
#Acceder a las llaves
for termino in diccionario.keys(): #ESta función permite regresar solo las llaves
    print(termino)
for valor in diccionario.values(): #Esta función permite regresar solo los valores
    print(valor)
#Acceder al valor
for termino, valor in diccionario.items(): #Esta función permite regresar los elementos separados por termino y valor
    print(termino, valor)
#Comprobar existencia de algún elemento
print('IdE' in diccionario) # No se encuentra ya que se debe de respetar mayúsculas y minúsculas
#Agregar elemento al diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)
#Remover un elemento
diccionario.pop('DBMS')
print(diccionario)
#limpiar el diccionario 
#diccionario.clear()
#print(diccionario)
#Eliminar el diccionario
# del diccionario
#print(diccionario)
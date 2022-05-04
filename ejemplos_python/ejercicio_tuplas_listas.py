#Se debe de crear una lista que solo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = [] # Se crea una lista vacía
for t in tupla:
    if t < 5:
       lista.append(t) # Se agrega a la lista los elementos menores a 5
print(lista)
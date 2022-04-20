#Manejo de Cadenas
misEquiposFavoritos = "América" + " y " + "Barcelona"  
print("Mis Equipos Favoritos son : " + misEquiposFavoritos) #Se utiliza el + para concatenar datos tipo str
print('___________________________________________________')
#Manejo de Cadenas con dos variables
miEquipoFavorito1 = 'América'
miEquipoFavorito2 = 'Barcelona'
print('Mis Equipos Favoritos son: ' + miEquipoFavorito1 + ' ' + miEquipoFavorito2)
#Imprimir sin concatenar variables
print('Mi Equipo Favorito es:', miEquipoFavorito1)
print('___________________________________________________')
#Error de Concatenación
numero1 = '5'
numero2 = '4'
print(numero1 + numero2)
numero1 = 5
numero2 = 4
print(numero1 + numero2)
print('Concatenación:', numero1 + numero2)
#Convertir una variable str a int
numero1 = '5'
numero2 = '4'
print('Suma:', int(numero1) + int(numero2))
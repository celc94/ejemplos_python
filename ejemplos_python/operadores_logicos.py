#Operadores Lógicos
import re
from httplib2 import ProxiesUnavailableError


a = False
b = False
#Operador and = Si las dos expresiones son verdaderas, el and devuelve verdadero
resultado = a and b
print(resultado) 
#Operador or = Si alguna variable es verdadera, el or devuelve verdadero
resultado = a or b
print(resultado)
#Operador not = cambia el valor de la variable
resultado = not a
print(resultado)
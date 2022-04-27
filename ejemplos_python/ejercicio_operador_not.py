#Ejercicio con el Operador not
#Preguntar si un padre puede asistir al juego del hijo.
#Puede asistir si tiene vacaciones o día de descanso, de lo contrario no puede asistir.

vacaciones = False
descanso = False

if not (vacaciones or descanso):
    print('Puede asistir al juego')
else:
    print('No puede asistir al juego')
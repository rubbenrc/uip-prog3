#-------------------------------------------------------------------------------
# Nombre:    tarea#2 AMBULANCIA
# Autor:      Rc
# Creado:     29/10/2015
# Copyright:   (c) programar 2015
# Licence:     <your licence 1.0>

# Crear un programa en python que resuelva el siguiente problema de fisica:
#Una ambulancia se mueve con una velocidad  de 120 km/h y necesita recorrer un
#tramo recto de 60 km.
#Calcular el tiempo necesario, en segundos, para que la ambulancia llegue a su
#destino. La formula a utilizar es: velocidad: distancia / tiempo.

#-------------------------------------------------------------------------------
import msvcrt
tiempo= int (120) #120km/h
distancia= int (60) #60km

velocidad= (tiempo)/(distancia)
print("""Una ambulancia se mueve con una velocidad  de 120 km/h y necesita recorrer un
tramo recto de 60 km.Calcular el tiempo necesario, en segundos,para que la
ambulancia llegue a su destino.\n""")
print "El tiempo necesario para que la ambulancia llegue a su destino es",velocidad,"segundos"

msvcrt.getch()


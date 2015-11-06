#-------------------------------------------------------------------------------
# Nombre:   tarea#3 umeros triangulares
# Autor:      rc
# Creado     29/10/2015
# Copyright:   (c) programar 2015
# Licence:     <your licence 1.1>

#Escriba un programa en Python donde el usuario introduce un n?mero n y el
#programa imprime los primeros n n?meros triangulares, junto con su ?ndice.
#Los n?meros triangulares se originan de la suma de los n?meros naturales desde
#1 hasta n.Ejemplo: Si se piden los primeros 3 n?meros triangulares, la salida
#es: 1 - 1 2 - 3 3 - 6

#-------------------------------------------------------------------------------
import msvcrt
numero=int(raw_input("introduzca un numero: "))
resultado={}
for i in range(1,numero+1):
    resultado[i]=(i*(i+1)/2)
for i in resultado:
    print i, resultado[i]

msvcrt.getch()




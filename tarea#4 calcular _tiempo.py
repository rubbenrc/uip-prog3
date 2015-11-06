#-------------------------------------------------------------------------------
# Name:        tarea 4 calcular dias, horas y minutos
# Auto:          rc
# Created:     29/10/2015
# Copyright:   (c) programar 2015
# Licence:     <your licence 1.2>

#Dado un intervalo de tiempo en minutos,
#calcular los d?as, horas y minutos correspondientes.

#?Que es main y como funciona?
# main es el bloque principal
#?Usando una declaraci?n?if?llamaremos a la funci?n?main?solo si el c?digo est?
# siendo ejecutado. En caso contrario, el c?digo solo?definir??la funci?n?main.
#El c?digo que lo haya importado podr? llamar a la funci?n cuando quiera.
#---------------------------------------------------------------------------

hora=int(input("Ingresa hora:"))
minutos=int(input("Ingresa minutos:"))
dia=int(input("Ingresa dia:"))

total_horas= hora*3600      #horas
total_minutos= minutos*60   #minutos
total_dia= dia*86400        #dias

print total_dia,"Dias",total_horas,"Horas",total_minutos,"Minutos"
input()



# Name:        tarea#6 encuesta
#
# Author:      programar
#
# Created:     30/10/2015
# Copyright:   (c) programar 2015
# Licence:     <your licence>

#Elaborar un programa en Python que encueste a 10 personas y las clasifique
#seg?n el deporte que practica.
#La lista de deportes v?lidos son: Ajedrez,Atletismo, Baloncesto, F?tbol, Karate
#, Nataci?n, Volleyball, Flag y Ping Pong.

#Puede darse el caso que no le guste ninguno de los deportes anteriores.
#Si es as?, entonces se puede seleccionar la opci?n Otros.
#Al final el programa debe mostrar estad?sticas de la encuesta e indicar
#cu?l es el deporte con mayor
# preferencia de los encuestados.
#-------------------------------------------------------------------------------
import msvcrt
#inicio
titulo="Encuesta Deportes\n".capitalize()
print titulo.center(50," ")
entrada= "Clasificacion de deportes que practican las personas\n"
print entrada.upper()
#-------------------------------------------------------------------------------
#pregunta
pregunta=0
c1=1
ajedrez=0
atletismo=0
futbol=0
baloncesto=0
karate=0
natacion=0
volleyball=0
flag=0
pingpong=0
otros=0

while pregunta >1 or pregunta <=10 :
    pregunta=pregunta+1
    print ("\n?Que deporte usted practica de la siguiente lista?\n ")
    print"1) Ajedrez"
    print'2) Atletismo'
    print'3) Baloncesto '
    print"4) Futbol"
    print"5) Karate "
    print"6) Natacion"
    print"7) Volleyball"
    print"8) Flag"
    print"9) Ping Pong"
    print"10) otros"
    opcion = int(raw_input('elija opcion: '))

    if opcion == 1:

        ajedrez=ajedrez+1
        print "\najedrez"

    elif opcion == 2:

        atletismo=atletismo+1
        print "\natletismo"

    elif opcion == 3:

        baloncesto=baloncesto+1
        print "\nbaloncesto"



    elif opcion == 4:

        futbol=futbol+1
        print "\nfutbol"

    elif opcion == 5:

        karate=karate+1
        print "\nkarate"


    elif  opcion == 6:

        natacion=natacion+1
        print "\nnatacion"


    elif  opcion == 7:

        volleyball=volleyball+1
        print "\nvolleybol"


    elif  opcion == 8:

        flag=flag+1
        print "\nflag"

    elif  opcion == 9:

        pingpong=pingpong+1
        print "\nping pong"

    elif opcion==10:

        otros=otros+1
        print"\notros"
    else:
        print"\nelija opciones establecidas"

    if pregunta >=10:
        break



print("\nEl total de encuestado de los diferentes deportes son:\n")
print("ajedrez",ajedrez)
print("atletismo:",atletismo)
print("baloncesto:",baloncesto)
print("futbol:",futbol)
print("karate:",karate)
print("natacion:",natacion)
print("volleyball:",volleyball)
print("flag:",flag)
print("pingpong",pingpong)
print("otros",otros)
msvcrt.getch()


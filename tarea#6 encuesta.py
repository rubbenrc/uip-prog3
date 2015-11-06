#-------------------------------------------------------------------------------
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
opcion=0
pregunta=0
c1=1
ct=1
nom=" "
while pregunta >1 or pregunta <=10 :
    pregunta=pregunta+1

    encuestado= input("\nEncuestado#"+str(ct)+"   ""Diga el numero de encuestado:")
    ct=encuestado+1
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
        ajedrez=("ajedrez")
        print ajedrez

    elif opcion == 2:

        atletismo= ('\n2) Atletismo')
        print atletismo

    elif opcion == 3:

        baloncesto= ('\n3) Baloncesto')
        print baloncesto
        print "\nbaloncesto"


    elif opcion == 4:

        futbol= ("\n4) Futbol")
        print futbol
        print "\nfutbol"

    elif opcion == 5:
        karate= ("\n5) Karate ")
        print karate
        print "\nkarate"


    elif  opcion == 6:
        natacion= ("\n6) Natacion")
        print natacion
        print "\nnatacion"


    elif  opcion == 7:

        volleyball= ("\n7) Volleyball")
        print volleyball
        print "\nvolleybol"


    elif  opcion == 8:
        por=100
        encuestado=10
        flag= ("\n8) Flag")
        print flag
        print "\nflag"

    elif  opcion == 9:

        pingpong= ("\n9) Ping Pong")
        print pingpong
        print "\nping pong"

    else:
        otros= ("\n10) otros")
        print otros

    if pregunta >=10:
        break

opcion = int(raw_input('elija opcion: '))

msvcrt.getch()

#----------------------------------------------------------------------------------------------------------
#profe no se como almacenar los datos que introduce el usuario
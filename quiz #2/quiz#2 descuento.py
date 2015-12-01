#-------------------------------------------------------------------------------
# Name:    descuento 
# Author:      rubben rc

# Creado:     10/11/2015
# Copyright:   (c) programar 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print"quiz#2"
import msvcrt
precio_original=0
descuento=0
monto_pagar=0

precio_original=(raw_input("diga el precio del articulo: "))
print "el precio introducido es:", precio_original,"$"


if monto_pagar > 100 and precio_original <=199:
     descuento=float(precio_original)*(10)/100
     print "el descuento es de:", descuento,"$"

     monto_pagar=float(precio_original)- float(descuento)
     print "el monto a pagar es:", monto_pagar,"$"

     print "descuento del 10%"

elif monto_pagar > 200 or monto_pagar <= 499:
    descuento=float(precio_original)*(20)/100
    print "el descuento es de:", descuento,"$"

    monto_pagar=float(precio_original)-float(descuento)
    print "el monto a pagar es:", monto_pagar,"$"

    print "descuento del 20%"

elif monto_pagar > 500:

    descuento=float(precio_original)*(30)/100
    print "el descuento es de:", descuento,"$"

    monto_pagar=float(precio_original)-float(descuento)
    print "el monto a pagar es: ", monto_pagar,"$"

    print "descuento del 30%"



msvcrt.getch()

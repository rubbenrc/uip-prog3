#-------------------------------------------------------------------------------
# Name:        Tarea#5 lista de supermercado de la empresa ABC
# Autor:      programar
#
# Creado:     30/10/2015
# Copyright:   (c) programar 2015
# Licence:     <your licence 1.2>

#Usted fue contratado por la startup ABC como programador.
#Ellos le solicitan que programe la primera fase de un mo?dulo que represente
#una lista de supermercados.
#El programa debe presentar un menu? donde pueda elegir, por lo poco, si quiero
#agregar, eliminar y ver los elementos de mi lista de supermercado.
#Se pueden manejar hasta 3 listas de supermercado.
#ABC esta? interesada en funciones, manejo de excepciones y m?dulos.
# Este c?digo debe servir para posteriores proyectos.
#-------------------------------------------------------------------------------

saludo="Hola Bienvenido a la Empresa ABC\n".capitalize()
print saludo.center(50," ")
entrada= "Programa para agregar,eliminar y ver la lista de supermercado\n"
print entrada.upper()
#------------------------------------------------------------------------------------------------------------
#menu agregar
import msvcrt
lista_supermercado_funciones=[]
lista_supermercado_manejo_excepciones=[]
lista_supermercado_modulos=[]

print 'Aque lista quiere agregarle un articulo?\n'
print '1) lista de supermercado funciones '
print '2) lista de supermercado excepciones'
print '3) lista de supermercado modulos'
print "4) ver lista de supermercados"
print "5) eliminar"

opcion = int(raw_input('elija opcion: '))

if opcion == 1:

        print("\nlista de supermercado funciones")
        lista_supermercado_funciones= [ (raw_input("Ingrese articulos a comprar: "))]
        print lista_supermercado_funciones

        lista_supermercado_funciones.append(raw_input("agregar otro elemento a la lista de supermecado: "))
        print lista_supermercado_funciones

elif opcion == 2:

       print ("\nlista de manejo de excepciones")
       lista_supermercado_manejo_excepciones= [(raw_input("Ingrese articulos a comprar: "))]
       print lista_supermercado_manejo_excepciones

       lista_supermercado_manejo_excepciones.append(raw_input("agregar otro elementos a la lista de supermecado:  "))
       print lista_supermercado_manejo_excepciones


elif opcion == 3:
       print("\nlistas de modulos")
       lista_modulos=[raw_input("Ingrese articulos a comprar: ")]
       print lista_modulos

       lista_modulos.append(raw_input("agregar otro elementos a la lista de supermecado:\n"  ))
       print lista_modulos
else:
    print("opcion invalida")

#-------------------------------------------------------------------------------------------------------------
#ver lista
x=lista_supermercado_funciones
x=lista_supermercado_manejo_excepciones
x=lista_supermercado_modulos

print("\nver lista")
if opcion == 4:

    print("Diga  a que lista quiesiera ver los articulos agregados ")
print '1) lista de supermercado funciones '
print '2) lista de supermercado excepciones'
print '3) lista de supermercado modulos'
opcion = int(raw_input('elija opcion: '))

if opcion == 1:
   lista_supermercado_funciones=[  ]
   for x in lista_supermercado_funciones:
    print x
    break
elif opcion == 2:
    lista_supermercado_manejo_excepciones=[ ]
    for x in lista_supermercado_manejo_excepciones:
     print x
     break
elif opcion == 3:
    lista_supermercado_modulos=[  ]
    for x in lista_supermercado_modulos:
     print x
     break
else:
    print "articulo no encontrado"

#-----------------------------------------------------------------------------------------------------------
#opcion 5 eliminar
lista_supermercado_funciones=[]
lista_supermercado_manejo_excepciones=[]
lista_supermercado_modulos=[]

print("\n eliminar")
if opcion == 5:

    print("Diga  a que lista quiere eliminarle articulos\n")
print ') lista de supermercado funciones '
print '2) lista de supermercado excepciones'
print '3) lista de supermercado modulos'
opcion = int(raw_input('elija opcion: '))

if opcion == 1:

    lista_supermercado_funciones=(raw_input("? Diga cual articulo quiere eliminar:"))
    print lista_supermercado_funciones

    lista_supermercado_funciones.remove(raw_input("? Diga cual otro articulo quiere eliminar:"))
    print lista_supermercado_funciones

elif opcion == 2:
    lista_supermercado_manejo_excepciones= (raw_input("? Diga cual articulo quiere eliminar:"))
    print lista_supermercado_manejo_excepciones

    lista_supermercado_manejo_excepciones.remove (raw_input("? Diga cual articulo quiere eliminar:"))
    print lista_supermercado_manejo_excepciones

elif opcion == 3:
    lista_supermercado_modulos=(raw_input("? Diga cual articulo quiere eliminar:"))
    print lista_supermercado_modulos

    lista_supermercado_modulos.remove (raw_input("? Diga cual articulo quiere eliminar:"))
    print lista_supermercado_modulos



else:
    print "articulo no encontrado"

msvcrt.getch()
#--------------------------------------------------------------------------------------------------------------------------------------
#profe no se como almacenar el dato introducido y como hacer ver la lista


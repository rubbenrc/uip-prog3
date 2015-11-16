#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      programar
#
# Created:     16/11/2015
# Copyright:   (c) programar 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import msvcrt
titulo="Empresa Rubben Rc Corporation\n".capitalize()
print titulo.center(50," ")
print("Telefono: 6948209")

class modelo_presupuesto:
    titulo="presupuesto"
    inicio_nombre="Empresa Rubben Rc Corporation"
    inicio_web= "www.rubbenrc.com"
    inicio_email= "rubbenrc@hotmail.com"

    cuota_iva= 7
    div= "="*80

    def set_cliente(self):
        self.empresa= raw_input("Empresa: ")
        self.cliente= raw_input("Nombre del cliente: ")

    def set_datos_basicos(self):
        self.fecha= raw_input(" Fecha: ")
        self.servicio= raw_input("Descripcion del servicio: ")
        importe= raw_input("importe bruto:  $")
        self.importe= float(importe)
        self.vencimiento= raw_input("fecha de expiracion: ")

    def iva(self):
         self.monto_iva= self.importe*self.cuota_iva/100
    def monto_neto(self):
        self.neto= self.importe+self.monto_iva

    def armar_presupuesto(self):
        """
            Esta funcion se encarga de armar todo el presupuesto
        """
        txt = '\n'+self.div+'\n'
        txt += '\t'+self.inicio_nombre+'\n'
        txt += '\tWeb Site: '+self.inicio_web+' | '
        txt += 'E-mail: '+self.inicio_email+'\n'
        txt += self.div+'\n'
        txt += '\t'+self.titulo+'\n'
        txt += self.div+'\n\n'
        txt += '\tFecha: '+self.fecha+'\n'
        txt += '\tEmpresa: '+self.empresa+'\n'
        txt += '\tCliente: '+self.cliente+'\n'
        txt += self.div+'\n\n'
        txt += '\tDetalle del servicio:'
        txt += '\t'+self.servicio+'\n\n'
        txt += '\tImporte: $%0.2f | IVA: $%0.2f\n' % (
                                  self.importe, self.monto_iva)
        txt += '-'*80
        txt += '\n\tMONTO TOTAL: $%0.2f\n' % (self.neto)
        txt += self.div+'\n'
        print txt

# Metodo constructor
    def __init__(self):
        print self.div
        print "\tPRESUPUESTO A OFRECER"
        print self.div
        self.set_cliente()
        self.set_datos_basicos()
        self.iva()
        self.monto_neto()
        self.armar_presupuesto()

# Instanciar clase
presupuesto =  modelo_presupuesto()

msvcrt.getch()

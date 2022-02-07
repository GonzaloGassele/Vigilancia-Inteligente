from ast import Del
from datetime import datetime
from mailbox import NoSuchMailboxError
from cv2 import resize
from Alert import SaveImage, telegram_msj

from vidgear.gears import CamGear

class camara():
    def __init__(self, nombre, source):
        self.nombre = nombre
        self.source = source
        self.estado = 0
    
    def getDatos(self):
        print(f"Nombre: {self.nombre} \n")

    def prenderCamara(self):
        if self.estado == 0:
            options = {'THREADED_QUEUE_MODE': False}
            CamGear(source=self.source,**options).start()
            print(f"Camara {self.nombre} encendida")
            self.estado=1
        #else:
            #print(f"La camara {self.nombre} ya estaba encendida")

    def leerCamara(self):
        options = {'THREADED_QUEUE_MODE': False}
        i=CamGear(source=self.source,**options).start()
        frames=i.read()
        return frames

    def apagarCamara(self):
        if self.estado==1:
            options = {'THREADED_QUEUE_MODE': False}
            CamGear(source=self.source,**options).stop()
            print(f"Camara {self.nombre} apagada")
        else:
            print(f"La camara {self.nombre} ya estaba apagada")
        



class telefono():
    def __init__(self, numero, nombre, chatid):
        self.numero = numero
        self.nombre = nombre
        self.chatid = chatid
        self.camaras = []
    
    def getDatos(self):
        print(f"Numero: {self.numero}")
        print(f"Nombre: {self.nombre}")
        print(f"Chat ID: {self.chatid}")
        print(f"Camaras asignadas: {self.camaras}")

    def asignarCamara(self, nombreCam):
        self.camaras.append(nombreCam)
    
    def removerCamara(self, nombreCam):
        count = 0 
        while count < len(self.camaras):
            if self.camaras[count]==nombreCam:
                self.camaras.remove(nombreCam)
                break
            count += 1



        


camaras=[]
telefonos=[]

def agregarCamara():
    print("Ingresar nombre de la camara:")
    nombre = input()
    print("Ingresar source de la camara:")
    source = input()
    camaras.append(camara(nombre,source))

def eliminarCamara():
    print("Ingresar nombre de la camara ha eliminar:")
    nombre = input()
    for i in range(len(camaras)):
        if camaras[i].nombre==nombre:
            del camaras[i]
            print("camara eliminada")
            break


def agregarTel():
    print("Ingresar numero de telefono:")
    numerotel = input()
    print("Ingresar nombre de la persona:")
    nombretel = input()
    telefonos.append(camara(numerotel,nombretel))

'''agregarCamara()
agregarCamara()

for i in range(len(camaras)):
    camaras[i].getDatos()
    #camaras[i].prenderCamara()

#eliminarCamara()

for i in range(len(camaras)):
    camaras[i].getDatos()
    camaras[i].apagarCamara()

for i in range(len(camaras)):
    camaras[i].detect()'''
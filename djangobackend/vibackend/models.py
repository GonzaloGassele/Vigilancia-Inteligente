from django.db import models
from vidgear.gears import CamGear

class camaraManager(models.Manager):

    def prenderCamara(self):
        if self.estado == False:
            options = {'THREADED_QUEUE_MODE': False}
            CamGear(source=self.source,**options).start()
            print(f"Camara {self.nombre} encendida")
            self.estado=True
        #else:
            #print(f"La camara {self.nombre} ya estaba encendida")

    def leerCamara(self):
        options = {'THREADED_QUEUE_MODE': False}
        i=CamGear(source=self.source,**options).start()
        frames=i.read()
        return frames

    def apagarCamara(self):
        if self.estado==True:
            options = {'THREADED_QUEUE_MODE': False}
            CamGear(source=self.source,**options).stop()
            print(f"Camara {self.nombre} apagada")
        else:
            print(f"La camara {self.nombre} ya estaba apagada")

class camara(models.Model):
    nombre = models.CharField(max_length=100)
    source = models.CharField(max_length=255)
    estado = models.BooleanField(default=False, blank=True)
    
    '''camaras= camaraManager()'''
    
    def __str__(self):
        return self.nombre


class telefono(models.Model):
    numero = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    chatid = models.CharField(max_length=20)
    camtel = models.ManyToManyField(camara)

    
    def __str__(self):
        return self.nombre



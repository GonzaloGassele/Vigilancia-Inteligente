from django.db import models
from django.contrib.auth.models import User
from .managers import AlertaManager, CamaraManager
from datetime import datetime
from cv2 import imwrite
from pathlib import Path

class Dia(models.Model):
    idDia= models.AutoField(primary_key=True)
    Dia = models.CharField(max_length=20)

class Horario(models.Model):
    idHorario = models.AutoField(primary_key=True)
    diaHorario = models.ForeignKey(Dia, on_delete=models.CASCADE)
    Horainicio = models.CharField(max_length=5,default="00:00")
    Horafin = models.CharField(max_length=5,default="23:59")
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        diahora= str(self.diaHorario.Dia)+" "+str(self.Horainicio)+" "+str(self.Horafin)
        return diahora


class Camara(models.Model):
    idCamara = models.AutoField(primary_key=True)    
    nombre = models.CharField(max_length=100)
    source = models.CharField(max_length=255)
    estado = models.BooleanField(default=False, blank=True)
    usercam = models.ForeignKey(User, on_delete=models.CASCADE)
    objects= CamaraManager()
    
    def __str__(self):
        return '%s, %s' % (self.nombre, self.source)

class Foto(models.Model):
    idFoto = models.AutoField(primary_key=True)
    path = models.ImageField(max_length=500, null = True, blank=True, upload_to='media/')
    etiqueta = models.BooleanField(null=True, blank=True)
    #camname = models.ForeignKey(Camara, on_delete=models.CASCADE) 
    camname = models.CharField(max_length=100)
    '''def SaveImage(self, img):
        date = datetime.now()
        year_month = date.strftime('%Y-%m-%d,%H-%M-%S')
        imwrite('media/'+year_month+'.jpg',img)
        self.path= Path('media/'+year_month+'.jpg')
        return self.path'''
    
    def __str__(self):
        return '%s, %s, %s' % (self.idFoto, self.etiqueta, self.camname)

class Telefono(models.Model):
    idTelefono = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    chatid = models.CharField(max_length=20, blank=True)
    usertel = models.ForeignKey(User, on_delete=models.CASCADE)
    fullDay = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return '%s, %s' % (self.nombre, self.numero)


class Camtel(models.Model):
    idCamtel = models.AutoField(primary_key=True)
    idCamara = models.ForeignKey(Camara, on_delete=models.CASCADE)
    idTelefono = models.ForeignKey(Telefono, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    activo = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return '%s' % (self.idCamtel)

class Camtelhorario(models.Model):
    idCamtelHorario = models.AutoField(primary_key=True)
    idCamtel = models.ForeignKey(Camtel, on_delete=models.CASCADE)
    idHorario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s, %s' % (self.idCamtelHorario, self.idCamtel, self.idHorario)

class Alerta(models.Model):
    idAlerta = models.AutoField(primary_key=True)
    idFoto = models.ForeignKey(Foto, on_delete=models.CASCADE, null=True, blank=True)
    idCamtelHorario = models.ForeignKey(Camtelhorario, on_delete=models.CASCADE)
    objects = AlertaManager()

    def __str__(self):
        return '%s, %s, %s' % (self.idAlerta, self.idCamtelHorario, self.idFoto)

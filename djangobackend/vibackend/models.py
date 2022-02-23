from http.client import LENGTH_REQUIRED
from django.db import models
from telegram import User
from vidgear.gears import CamGear
from django.contrib.auth.models import User, UserManager
from .managers import CamaraManager, FotoManager

class Horario(models.Model):
    dia = models.IntegerField()
    Horainicio = models.TimeField()
    Horafin = models.TimeField()

    def __str__(self):
        diahora= str(self.dia)+" "+str(self.Horainicio)+" "+str(self.Horafin)
        return diahora

class Skedul(models.Model):
    idHorario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        horasuario=str(self.idHorario)+" "+str(self.idUsuario)
        return horasuario

class Camara(models.Model):
    nombre = models.CharField(max_length=100)
    source = models.CharField(max_length=255)
    estado = models.BooleanField(default=False, blank=True)
    usercam = models.ForeignKey(User, on_delete=models.CASCADE)
    objects= CamaraManager()
    
    def __str__(self):
        return self.nombre


class Foto(models.Model):
    idFoto = models.IntegerField(primary_key=True)
    path = models.CharField(max_length=255, editable=False)
    etiqueta = models.CharField(max_length=2,null=True, blank=True)
    camname = models.ForeignKey(Camara, on_delete=models.CASCADE)
    objects= FotoManager()
    
    def __str__(self):
        return str(self.idFoto)

class Telefono(models.Model):
    numero = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    chatid = models.CharField(max_length=20)
    usertel = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Camtel(models.Model):
    idCamara = models.ForeignKey(Camara, on_delete=models.CASCADE)
    idTelefono = models.ForeignKey(Telefono, on_delete=models.CASCADE)
    idSkedul = models.ForeignKey(Skedul, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        camret=str(self.idCamara)+" "+str(self.idTelefono)+" "+str(self.idSkedul)
        return camret

class Alerta(models.Model):
    idFoto = models.ForeignKey(Foto, on_delete=models.CASCADE, null=True, blank=True)
    idCamtel = models.ForeignKey(Camtel, on_delete=models.CASCADE)

    def __str__(self):
        alereturn=str(self.id)+" "+str(self.idCamtel)
        return alereturn

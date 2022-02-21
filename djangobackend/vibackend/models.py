from http.client import LENGTH_REQUIRED
from django.db import models
from telegram import User
from vidgear.gears import CamGear
from django.contrib.auth.models import AbstractBaseUser
from .managers import UsuarioManager


class Usuario(AbstractBaseUser):
    username = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    objects= UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        full_name = "{0}".format(self.username)
        return full_name.strip()

    def get_short_name(self):
        return self.username

class Horario(models.Model):
    dia = models.DateField()
    Horainicio = models.TimeField()
    Horafin = models.TimeField()

    def __str__(self):
        return self.dia.strftime('%A')

class Skedul(models.Model):
    idHorario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        horasuario=str(self.idHorario)+" "+str(self.idUsuario)
        return horasuario

class Camara(models.Model):
    nombre = models.CharField(max_length=100)
    source = models.CharField(max_length=255)
    estado = models.BooleanField(default=False, blank=True)
    usercam = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


class Foto(models.Model):
    idFoto = models.IntegerField(primary_key=True)
    etiqueta = models.CharField(max_length=2,null=True, blank=True)
    camname = models.ForeignKey(Camara, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.idFoto

class Telefono(models.Model):
    numero = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    chatid = models.CharField(max_length=20)
    usertel = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Camtel(models.Model):
    idCamara = models.ForeignKey(Camara, on_delete=models.CASCADE)
    idTelefono = models.ForeignKey(Telefono, on_delete=models.CASCADE)
    idSkedul = models.ForeignKey(Skedul, on_delete=models.CASCADE)

    def __str__(self):
        camret=str(self.idCamara)+" "+str(self.idTelefono)+" "+str(self.idSkedul)
        return camret

class Alerta(models.Model):
    idFoto = models.ForeignKey(Foto, on_delete=models.CASCADE, null=True, blank=True)
    idCamtel = models.ForeignKey(Camtel, on_delete=models.CASCADE)

    def __str__(self):
        alereturn=str(self.id)+" "+str(self.idCamtel)
        return alereturn

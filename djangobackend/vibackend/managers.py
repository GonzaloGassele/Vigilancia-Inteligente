from multiprocessing.sharedctypes import Value
from django.contrib.auth.models import BaseUserManager
from django.db import models
from vidgear.gears import CamGear
from datetime import datetime
from cv2 import imwrite
from pathlib import Path
import telegram
import telegram.ext

bot_token = '5265828925:AAHrKJS0mz0AnAciJxOSWQ53aQo69AizEfM'
#api_url= f"https://api.telegram.org/bot{bot_token}/"
bot= telegram.ext.ExtBot(token= bot_token)

class CamaraManager(models.Manager):

    def leerCamara(self):
        options = {'THREADED_QUEUE_MODE': False}
        i=CamGear(source=self.source,**options).start()
        frames=i.read()
        return frames


class FotoManager(models.Manager):
    
    def SaveImage(img):
        date = datetime.now()
        year_month = date.strftime('%Y-%m-%d,%H-%M-%S')
        imwrite('fotos/'+year_month+'.jpg',img)
        img_path= Path('fotos/'+year_month+'.jpg')
        return img_path



class AlertaManager(models.Manager):
    def telegram_msj(num ,text , img_path):
        img= open(img_path,'rb')
        bot.sendPhoto(chat_id= num,photo= img,caption= text)



# class CamtelManager(models.Manager):
#     def crear_camara(self, nombre, source):
#         if not source:
#             raise ValueError('Camara debe tener una direccion source')
        
#         camara = self.model(nombre=nombre)
#         camara = self.model(source=source)
#         camara.save()
#         return camara
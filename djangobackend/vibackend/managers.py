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

    
    '''def monitoreo(self):
            date = datetime.now()
            dia = int(date.strftime('%w'))
            hour= int(date.strftime('%H'))
            minute=int(date.strftime('%M'))

            if dia==self.idCamtelHorario.idHorario.Dia

            listhoraini=self.idCamtelHorario.idHorario.Horainicio.split(':')
            horaini = int (listhoraini[0])
            minini = int (listhoraini[1])
            listhorafin=self.idCamtelHorario.idHorario.Horafin.split(':')
            horafin = int (listhorafin[0])
            minfin = int (listhorafin[1])

            if (hour>=horaini and hour<=horafin) and (minute>=minini and minute<=minfin):'''

    def telegram_msj(num ,text , img_path):
        img= open(img_path,'rb')
        bot.sendPhoto(chat_id= num,photo= img,caption= text)


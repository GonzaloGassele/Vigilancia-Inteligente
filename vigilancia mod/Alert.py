from datetime import datetime
from cv2 import imwrite
from pathlib import Path
import telegram

def SaveImage(img):
    date = datetime.now()
    year_month = date.strftime('%Y-%m-%d,%H-%M-%S')
    imwrite('C:/Users/PCT-02/Proyectos visual studio/repositorios/Vigilancia-inteligente/detect/'+year_month+'.png',img)
    img_path= Path('detect/'+year_month+'.png')
    return img_path

bot_token = '5265828925:AAHrKJS0mz0AnAciJxOSWQ53aQo69AizEfM'
bot= telegram.Bot(token= bot_token)
def telegram_msj(num ,text , img_path):
    img= open(img_path,'rb')
    bot.sendPhoto(chat_id= num,
                photo= img,
                caption= text)

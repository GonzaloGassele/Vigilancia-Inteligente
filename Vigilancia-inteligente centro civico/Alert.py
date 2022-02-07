from datetime import datetime
from cv2 import imwrite
from pathlib import Path
import telegram

def SaveImage(img):
    date = datetime.now()
    year_month = date.strftime('%Y-%m-%d,%H-%M-%S')
    imwrite('/home/ia1/cv/Proyectos/Vigilancia-Inteligente/detect/'+year_month+'.png',img)
    img_path= Path('detect/'+year_month+'.png')
    return img_path

bot_token = '5087135434:AAEGb6ZpL_tT2qzkW99XSaVHO7cNipyRbEU'
bot= telegram.Bot(token= bot_token)
agenda= ['5154270959']
def telegram_msj(num ,text , img_path):
    img= open(img_path,'rb')
    bot.sendPhoto(chat_id= num,
                photo= img,
                caption= text)


from datetime import datetime
from cv2 import imwrite
from pathlib import Path
from pywhatkit import sendwhats_image

def SaveImage(img):
    date = datetime.now()
    year_month = date.strftime('%Y-%m-%d,%H-%M-%S')
    imwrite('/home/ia1/cv/Proyectos/Vigilancia-Inteligente/detect/'+year_month+'.png',img)
    img_path= Path('detect/'+year_month+'.png')
    return img_path

def send_msj1(t, img_path):
    sendwhats_image(phone_no='+5492392611662',#Monitoreo urbano
                        img_path= img_path,
                        caption= t,
                       tab_close=True)
def send_msj2(t, img_path):
    sendwhats_image(phone_no='+5492392524855',#Ricardo Machado
                        img_path= img_path,
                        caption= t,
                        tab_close=True)
def send_msj3(t, img_path):
   sendwhats_image(phone_no='+5492392489549',# Juan Sereno
                        img_path= img_path,
                        caption= t,
                        tab_close=True)
def send_msj4(t, img_path):
    sendwhats_image(phone_no='+5492392315672',#Cel Polo (Brisuela)
                        img_path= img_path,
                        caption= t,
                        tab_close=True)
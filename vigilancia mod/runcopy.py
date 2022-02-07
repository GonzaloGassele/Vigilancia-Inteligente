import subprocess as sp
from datetime import datetime
from clases import camara, telefono, camaras, telefonos
from torch.hub import load
from Alert import SaveImage , telegram_msj
from cv2 import resize
from funciones import camaraAsignar, camaraRemover
import sys


#base de tiempo
date = datetime.now()
hour= int(date.strftime('%H'))
minute=int(date.strftime('%M'))

#extProc = sp.Popen(['python','C:/Users/PCT-02/Proyectos visual studio/repositorios/Vigilancia-inteligente/clases.py']) # ejecuta myPyScript.py 

#status = sp.Popen.poll(extProc) # status debería ser 'None' al correr

def tiempo():
    global date, hour, minute
    date = datetime.now()
    hour= int(date.strftime('%H'))
    minute=int(date.strftime('%M'))

camaras.append(camara('Frente','rtsp://contralor:Villegas555@100.100.34.184/cgi-bin/main.cgi'))
camaras.append(camara('Atras','rtsp://contralor:Villegas555@100.100.34.183/cgi-bin/main.cgi'))
camaras.append(camara('Galpon','rtsp://contralor:Villegas555@192.168.103.149/cgi-bin/main.cgi'))
camaras.append(camara('Costado del Polo','rtsp://contralor:Villegas555@100.100.34.179/cgi-bin/main.cgi'))
camaras.append(camara('Estacionamiento de emision','rtsp://contralor:Villegas555@192.168.103.233/cgi-bin/main.cgi'))
camaras.append(camara('Sector de baños','rtsp://contralor:Villegas555@192.168.103.234/cgi-bin/main.cgi'))
camaras.append(camara('Entrada de Pacheco','rtsp://contralor:Villegas555@192.168.102.105/cgi-bin/main.cgi'))
camaras.append(camara('Entrada de Pacheco 2','rtsp://contralor:Villegas555@192.168.102.98/cgi-bin/main.cgi'))
telefonos.append(telefono(5492392502978,'Gonzalo',1645237568))
telefonos.append(telefono(0,'M',0))


camaraAsignar('Frente','Gonzalo')
camaraAsignar('Galpon','Gonzalo')
camaraAsignar('Estacionamiento de emision','Gonzalo')
camaraAsignar('Costado del Polo','Gonzalo')
for i in range(len(telefonos)):
    telefonos[i].getDatos()

camaraRemover('Estacionamiento de emision','Gonzalo')
for i in range(len(telefonos)):
    telefonos[i].getDatos()

model= load('ultralytics/yolov5', 'yolov5s6')# modelo

#configuración del modelo
model.conf = 0.1#confidence threshold (0-1)
model.classes= [0]# detección de personas

while True:
    tiempo()
    #intervalo de ejecucion
    if hour>=8 or hour<=12:
        #if sp.Popen.poll(extProc) != None:
            #extProc = sp.Popen(['python','C:/Users/PCT-02/Proyectos visual studio/repositorios/Vigilancia-inteligente/clases.py'])
        for j in range(len(telefonos)):
            for i in range(len(camaras)):
                frame=camaras[i].leerCamara()
                print("la camara esta leyendo los datos")
                if None is frame:
                    frame=camaras[i].leerCamara()
                else:
                    try:
                        img= resize(frame ,(0,0),fx=0.3,fy=0.3)
                        texto= camaras[i].nombre
                        result= model(img)
                        result.render() 
                        labels = result.xyxyn[0][:, -1].cpu().numpy()
                
                        if (labels.all()==0):
                            print(texto)
                            img_path= SaveImage(img)
                            t=str('Hay una persona en la camara de '+ camaras[i].nombre)
                            for tel in range(len(telefonos)):
                                for k in range(len(telefonos[tel].camaras)):
                                    if telefonos[tel].camaras[k] == camaras[i].nombre:
                                        telegram_msj(telefonos[tel].chatid,t,img_path)
                    except:
                        print("ocurrio un error: ")
                        e = sys.exc_info()[1]
                        print(e.args[0])

    #intervalo de detencion        
    #if sp.Popen.poll(extProc) == None:    
    if hour<8 and hour>12:
        for i in range(len(camaras)):
            camaras[i].apagarCamara()    
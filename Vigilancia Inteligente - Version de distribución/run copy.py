import subprocess as sp
from datetime import datetime
from clases import agregarCamara, camara, telefono, camaras, telefonos


#base de tiempo
date = datetime.now()
hour= int(date.strftime('%H'))
minute=int(date.strftime('%M'))

extProc = sp.Popen(['python','C:/Users/PCT-02/Proyectos visual studio/repositorios/Vigilancia-inteligente/clases.py']) # ejecuta myPyScript.py 

#status = sp.Popen.poll(extProc) # status debería ser 'None' al correr

def tiempo():
    global date, hour, minute
    date = datetime.now()
    hour= int(date.strftime('%H'))
    minute=int(date.strftime('%M'))

camaras.append(camara('Frente','rtsp://contralor:Villegas555@100.100.34.184/cgi-bin/main.cgi'))
camaras.append(camara('Atras','rtsp://contralor:Villegas555@100.100.34.183/cgi-bin/main.cgi'))
telefonos.append(telefono(5492392502978,'Gonzalo',1645237568))

while True:
    tiempo()
    #intervalo de ejecucion
    if hour>=8 or hour<=12:
        #if sp.Popen.poll(extProc) != None:
            #extProc = sp.Popen(['python','C:/Users/PCT-02/Proyectos visual studio/repositorios/Vigilancia-inteligente/clases.py'])
        for j in range(len(telefonos)):
            for i in range(len(camaras)):
                camaras[i].prenderCamara()
                camaras[i].detect(telefonos[j])

    #intervalo de detencion        
    if sp.Popen.poll(extProc) == None:    
        if hour<8 and hour>12:    
            sp.Popen.terminate(extProc)# cierre del proceso

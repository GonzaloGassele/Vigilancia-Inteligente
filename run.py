import subprocess as sp
from datetime import datetime


#base de tiempo
date = datetime.now()
hour= int(date.strftime('%H'))
minute=int(date.strftime('%M'))

extProc = sp.Popen(['python','/home/ia1/cv/Proyectos/Vigilancia-Inteligente/model.py']) # ejecuta myPyScript.py 

#status = sp.Popen.poll(extProc) # status debería ser 'None' al correr

def tiempo():
    global date, hour, minute
    date = datetime.now()
    hour= int(date.strftime('%H'))
    minute=int(date.strftime('%M'))

while True:
    tiempo()
    #intervalo de ejecucion
    if hour>=19 or hour<=4:
        if sp.Popen.poll(extProc) != None:
            extProc = sp.Popen(['python','/home/ia1/cv/Proyectos/Vigilancia-Inteligente/model.py'])

    #intervalo de detencion        
    if sp.Popen.poll(extProc) == None:    
        if hour<19 and hour>4:    
            sp.Popen.terminate(extProc)# cierre del proceso
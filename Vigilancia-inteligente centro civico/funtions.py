from vidgear.gears import CamGear

options = {"CAP_PROP_BUFFERSIZE": 0,'THREADED_QUEUE_MODE': False}

def active_cam():
    cap=[[0,1,0],[1,1,0],[2,1,0]]
    cap[0][1]=CamGear(source='rtsp://contralor:Villegas555@172.20.20.152/cgi-bin/main.cgi',**options).start()
    cap[1][1]=CamGear(source='rtsp://contralor:Villegas555@172.20.20.160/cgi-bin/main.cgi',**options).start()
    cap[2][1]=CamGear(source='rtsp://contralor:Villegas555@172.20.20.159/cgi-bin/main.cgi',**options).start()#Centro Civico
    
    cap[0][2]= 'Hay una persona en el centro civico'
    cap[1][2]='Hay una persona en el centro civico'
    cap[2][2]='Hay una persona en el centro civico'
    
    return cap

def read_camera (cap):
    frames=[[0,3],[1,3],[2,3]]
    for j ,i ,t in cap: 
        frames[j][0]=i.read()
        frames[j][1]= [t]
    return frames

def stop_cam(cap):
    cap[0][1].stop()
    cap[1][1].stop()
    cap[2][1].stop()
    cap[3][1].stop()
  



from cv2 import resize
from torch.hub import load
import funtions as f
from Alert import SaveImage , telegram_msj, agenda


def detect():

    model= load('ultralytics/yolov5', 'yolov5x6')# modelo

#configuración del modelo
    model.conf = 0.75#confidence threshold (0-1)
    model.classes= [0]# detección de personas

    cap=f.active_cam()


    while(True):
        frame=f.read_camera(cap)
        if None is frame:
            frame=f.read_camera(cap)
        else:
            for i in frame:
                try:
                    img= resize(i[0] ,(0,0),fx=0.3,fy=0.3)
                    texto= i[1]
                    result= model(img, augment= True)
                    result.render() 
                    labels = result.xyxyn[0][:, -1].cpu().numpy()
                    
                    if (labels.all()==0):
                        print(texto)
                        img_path= SaveImage(img)
                        t=str(texto[0])
                        for tel in agenda:
                            telegram_msj(tel,t,img_path)
                except:
                    pass

detect()

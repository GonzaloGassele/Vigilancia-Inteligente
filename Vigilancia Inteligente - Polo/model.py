from cv2 import resize
from torch.hub import load
import funtions as f
from Alert import SaveImage , telegram_msj, agenda


def detect():

    model= load('ultralytics/yolov5', 'yolov5s6','yolov5x6')# modelo


#configuración del modelo
    model.conf = 0.80#confidence threshold (0-1)
    model.classes= [0]# detección de personas
    model.amp= True
    cap=f.active_cam()


    while(True):
        frame=f.read_camera(cap)
        if None is frame:
            frame=f.read_camera(cap)
        else:
            for i in frame:
                try:
                    img= resize(i[0] ,(1280,720))
                    texto= i[1]
                    result= model(img, augment=True)
                     
                    labels = result.xyxyn[0][:, -1].cpu().numpy()
                    boxes = result.pandas().xyxy[0]
                    if (labels.all()==0):
                        print(texto)
                        img_path, year_month = SaveImage(img)
                        t=str(texto[0])
                        f.save_txt(boxes,img,year_month)
                        for tel in agenda:
                            telegram_msj(tel,t,img_path)
                except:
                    print('Algo salio mal')
                    pass
detect()

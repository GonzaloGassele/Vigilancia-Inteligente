from vidgear.gears import CamGear

cam_vector= []

class camaras:
    def __init__(self,direccion,ubicacion):
        self.direccion = direccion
        self.ubicacion = ubicacion

    def agregar_cam(direccion, ubicacion, cam_vector):
        cam_vector.append([direccion,ubicacion])
    

    def inicio(direccion, ubicacion, cam_vector):
        cap=[]
        options = {'THREADED_QUEUE_MODE': False}
        for i in cam_vector:
            camara= CamGear(source= str(i[0]),**options).start()
            cap.append([camara,ubicacion])
        return cap

    def read_camera (cap):
        frames= [*range(len(cap))]
        text= [*range(len(cap))]
        for i in range(len(cap)): 
            frames[i]= cap[i][0].read()
            text[i] = cap[i][1]
        return frames

    def stop_cam(cap):
        for i in range(len(cap)):
            cap[i][0].stop()



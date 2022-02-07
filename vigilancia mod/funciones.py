from clases import camara, telefono, camaras, telefonos

def camaraAsignar(nombreCam, nombreTel):
    for j in range(len(camaras)):
        if camaras[j].nombre==nombreCam:
            indice=j
    for i in range(len(telefonos)):
        if telefonos[i].nombre==nombreTel:
            telefonos[i].asignarCamara(camaras[indice].nombre) 

def camaraRemover(nombreCam, nombreTel):
    for j in range(len(camaras)):
        if camaras[j].nombre==nombreCam:
            indice=j
    for i in range(len(telefonos)):
        if telefonos[i].nombre==nombreTel:
            telefonos[i].removerCamara(camaras[indice].nombre) 
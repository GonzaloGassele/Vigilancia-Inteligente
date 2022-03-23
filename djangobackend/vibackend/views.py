from django.views import View
from .models import Camara, Camtel, Telefono, Horario, Alerta, Foto, Dia, Camtelhorario
from django.shortcuts import render, redirect
from vidgear.gears import CamGear
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import datetime
from cv2 import resize, imwrite
from torch.hub import load
import telegram
import telegram.ext
import sys
from pathlib import Path
from django.core.paginator import Paginator
from django.urls import reverse_lazy


bot_token = '5265828925:AAHrKJS0mz0AnAciJxOSWQ53aQo69AizEfM'
#api_url= f"https://api.telegram.org/bot{bot_token}/"
bot= telegram.ext.ExtBot(token= bot_token)

def index(request):
        
    return render(request, "index.html")


def arranque(request):
    model= load('ultralytics/yolov5', 'yolov5s6')# modelo
    #configuración del modelo
    model.conf = 0.1#confidence threshold (0-1)
    model.classes= [0]# detección de personas
    camaras = Camara.objects.filter(estado=True).filter(usercam=request.user).all()
    k=[]
    for i in camaras:
        if i.estado:
            options = {'THREADED_QUEUE_MODE': False,'CAP_PROP_FPS': 1}
            k.append([i.nombre,CamGear(source=i.source,**options).start()])

    while True:
        #print(camaras)
        for i in camaras:
            frames=None
            #frame=Camara.objects.get(idCamara=i.idCamara).leerCamara()
            
            if i.estado:
                for j in k:
                    if i.nombre==j[0]:
                        print(j[0])
                        print(i.nombre)
                        print("entro")
                        frames=j[1].read()
                print(f"la camara {i.nombre} esta leyendo los datos")
            else:
                print("Laucha")
            if None is frames:
                print("no encuentra frames")
            else:
                try:
                    print("try")
                    img= resize(frames ,(0,0),fx=0.3,fy=0.3)
                    texto= i.nombre
                    result= model(img)
                    result.render() 
                    labels = result.xyxyn[0][:, -1].cpu().numpy()

                    if (labels.all()==0):
                        print("ENTRO AL LABELLL")
                        print(texto)
                        foto=Foto.objects.create(camname=i)
                        foto.SaveImage(img)
                        t=str('La camara detecto una persona en '+ i.nombre)
                        camtel = Camtel.objects.filter(idCamara=i.idCamara).all()
                        for ct in camtel:
                            if ct.activo:
                                Tel = Telefono.objects.get(idTelefono=ct.idTelefono.idTelefono)
                                print(Tel)
                                print(Tel.chatid)
                                print("AHI VA LA ALERTA")
                                #Alerta.objects.telegram_msj(Tel.chatid,t,img_path)
                                #img= open(img_path,'rb')
                                bot.sendPhoto(chat_id= Tel.chatid, photo= img,caption= t)
                                #bot.sendMessage(chat_id=Tel.chatid, text=t)

                except:
                    print("ocurrio un error: ")
                    e = sys.exc_info()[1]
                    print(e.args[0])



def autenticar(request):
    username = request.POST['username']
    password = request.POST['password']
    usuario = authenticate(request, username=username, password=password)
    if usuario is not None:
        login(request, usuario)
        return redirect('/vibackend/index/')
    else:
        return redirect('/vibackend/login/')
 
def loguear(request):
    return render(request, "login.html")

def autenticarRegistro(request):
    username = request.POST['username']
    email = request.POST['mail']
    password = request.POST['password']
    usuario = User.objects.create_user(username=username, email=email, password=password)
    return redirect('/vibackend/login/')
 
def registrar(request):
    return render(request, "registro.html")

def desloguear(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/vibackend/login/')

class CamaraView(LoginRequiredMixin ,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def home(request):
        camaraListados = Camara.objects.filter(usercam=request.user)
        return render(request, "gestionCamaras.html", {'camara': camaraListados,})


    def registrarCamara(request):
        nombre = request.POST['txtNombre']
        source = request.POST['txtSource']
        camara = Camara.objects.create(
            nombre=nombre, source=source , estado = False, usercam=request.user)
        return redirect('/vibackend/camara/')

    def edicionCamara(request, idCamara):
        camara = Camara.objects.filter(usercam=request.user).get(idCamara=idCamara)
        return render(request, "edicionCamara.html", {"camara": camara})


    def editarCamara(request):
        nombre = request.POST['txtNombre']
        source = request.POST['txtSource']
        idCamara = request.POST['idCamara']

        camara = Camara.objects.filter(usercam=request.user).get(idCamara=idCamara)
        camara.nombre = nombre
        camara.source = source
        camara.save()

        return redirect('/vibackend/camara/')

    def eliminarCamara(request, idCamara):
        camara = Camara.objects.filter(usercam=request.user).get(idCamara=idCamara)
        camara.delete()


        return redirect('/vibackend/camara/')

    def prenderCamara(request, idCamara):
        camara = Camara.objects.filter(usercam=request.user).get(idCamara=idCamara)
        if camara.estado == False:
            camara.estado=True
            camara.save()
        return redirect('/vibackend/camara/')


    def apagarCamara(request, idCamara):
        camara = Camara.objects.filter(usercam=request.user).get(idCamara=idCamara)
        if camara.estado==True:
            camara.estado=False
            camara.save()
        return redirect('/vibackend/camara/')


class TelefonoView(LoginRequiredMixin, View):
    login_url = '/vibackend/login/'
    redirect_field_name = 'redirect_to'

    def home(request):
        telefonoListados = Telefono.objects.filter(usertel=request.user)
        return render(request, "gestionTelefonos.html", {'telefono': telefonoListados,})


    def registrarTelefono(request):
        nombre = request.POST['txtNombre']
        numero = request.POST['txtNumero']
        telefono = Telefono.objects.create(
            nombre = nombre, numero = numero, usertel=request.user
        )
        return redirect('/vibackend/telefono/')

    def eliminarTelefono(request, idTelefono):
        telefono = Telefono.objects.filter(usertel=request.user).get(idTelefono = idTelefono)
        telefono.delete()
        return redirect('/vibackend/telefono/')

    def edicionTelefono(request, idTelefono):
        telefono = Telefono.objects.filter(usertel=request.user).get(idTelefono = idTelefono)
        return render(request, "edicionTelefono.html", {"telefono": telefono})

    def editarTelefono(request):
        nombre = request.POST['txtNombre']
        numero = request.POST['txtNumero']
        idTelefono = request.POST['idTelefono']
        telefono = Telefono.objects.filter(usertel=request.user).get(idTelefono = idTelefono)
        telefono.nombre = nombre
        telefono.numero = numero
        telefono.save()

        return redirect('/vibackend/telefono/')

class HorarioView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def home(request):
        diaListados = Dia.objects.all()
        horarioListados = Horario.objects.filter(idUsuario=request.user)
        a = horarioListados.count()
        if a < 7:
            for i in diaListados:
                Horario.objects.create(diaHorario=i, Horainicio="12:00", Horafin="23:59", idUsuario=request.user)
        return render(request, "HorariosPrueba.html", {'dia': diaListados, 'horario': horarioListados,})


    def editarHorario(request):
        diaListados = Dia.objects.all()
        for i in diaListados:
            k=i.idDia
            dia = Dia.objects.get(idDia=request.POST[f'numDia{k}'])
            horainicio = request.POST[f'timeHoraIni{k}']
            horafin = request.POST[f'timeHoraFin{k}']

            horario = Horario.objects.filter(idUsuario=request.user).get(idHorario=request.POST[f'idHorario{k}'])
            horario.dia = dia
            horario.Horainicio = horainicio
            horario.Horafin = horafin
            horario.save()

        return redirect('/vibackend/horario/')


class AlertaView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def home(request):
        telefonoListados = Telefono.objects.filter(usertel=request.user).all()
        camaraListados = Camara.objects.filter(usercam=request.user).all()
        for t in telefonoListados:
            for c in camaraListados:
                try:
                    Camtel.objects.get(idTelefono=t, idCamara=c, idUsuario=request.user)
                except Camtel.DoesNotExist:
                    Camtel.objects.create(idTelefono=t, idCamara=c, idUsuario=request.user)
        horarioListados = Horario.objects.filter(idUsuario=request.user).all()
        camtelListados = Camtel.objects.filter(idUsuario=request.user).all()
        for h in horarioListados:
            for ct in camtelListados:
                try:
                    Camtelhorario.objects.get(idCamtel=ct, idHorario=h)
                except Camtelhorario.DoesNotExist:
                    Camtelhorario.objects.create(idCamtel=ct, idHorario=h)
        cmhListado = Camtelhorario.objects.filter(idCamtel__idUsuario=request.user).all()
        for ch in cmhListado:
            try:
                Alerta.objects.get(idCamtelHorario=ch)
            except Alerta.DoesNotExist:
                Alerta.objects.create(idCamtelHorario=ch)
        alertaListados = Alerta.objects.filter(idCamtelHorario__idCamtel__idUsuario=request.user).all()
        return render(request, "Alertas.html", {'alerta': alertaListados, 'cthorario': cmhListado, 'camtel': camtelListados, 'telefono': telefonoListados, 'camara': camaraListados,'horario': horarioListados,})

    def fullTime(request,idTelefono):
        telefono = Telefono.objects.get(idTelefono=idTelefono)
        if telefono.fullDay == False:
            telefono.fullDay=True
            telefono.save()
        elif telefono.fullDay == True:
            telefono.fullDay=False
            telefono.save()
        return redirect('/vibackend/alerta/')

    def editarAlerta(request, idCamtel):
        camtel = Camtel.objects.filter(idUsuario=request.user).get(idCamtel=idCamtel)
        if camtel.activo == False:
            camtel.activo=True
            camtel.save()
        elif camtel.activo == True:
            camtel.activo=False
            camtel.save()
        else:
            print("error")
        return redirect('/vibackend/alerta/')
        



class FotoView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def pruebaFoto(request):
        foto1 = Foto.objects.all()

        foto_paginator = Paginator(foto1, 5)

        numero_pagina = request.GET.get('pagina')
        pagina = foto_paginator.get_page(numero_pagina)

        return render(request, "fotos.html", {"foto" : foto1, 'pagina': pagina})

    def confirmarFoto(request, idFoto, confirmacion, pagina):
        foto = Foto.objects.get(idFoto = idFoto)
        foto.etiqueta = confirmacion
        foto.save()


        url = reverse_lazy("pruebaFoto") + "?pagina=" + pagina
        
        return redirect(url)
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Camara, Skedul, Telefono, Horario, Alerta, Foto
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
from vidgear.gears import CamGear

def index(request):
    return HttpResponse("Hello, world. You're at the Vigilancia Inteligente index.")


class CamaraView(View):

    def home(request):
        camaraListados = Camara.objects.all()
        messages.success(request, '¡Camaras listadas!')
        return render(request, "gestionCamaras.html", {"Camaras": camaraListados})


    def registrarCamara(request):
        nombre = request.POST['txtNombre']
        source = request.POST['txtsource']
        camara = Camara.objects.create(
            nombre=nombre, source=source, estado = False)
        messages.success(request, '¡Camara registrada!')
        return redirect('/')


    def edicionCamara(request, nombre):
        camara = Camara.objects.get(nombre=nombre)
        return render(request, "edicionCamara.html", {"camara": camara})


    def editarCamara(request):
        nombre = request.POST['txtNombre']
        source = request.POST['txtsource']

        camara = Camara.objects.get(nombre=nombre)
        camara.nombre = nombre
        camara.source = source
        camara.save()

        messages.success(request, '¡Camara actualizada!')

        return redirect('/')


    def eliminarCamara(request, nombre):
        camara = Camara.objects.get(nombre=nombre)
        camara.delete()

        messages.success(request, '¡Camara eliminada!')

        return redirect('/')

    def prenderCamara(request, nombre):
        camara = Camara.objects.get(nombre=nombre)
        if camara.estado == False:
            options = {'THREADED_QUEUE_MODE': False}
            CamGear(source=camara.source,**options).start()
            messages.success(request, f'Camara {camara.nombre} encendida')
            camara.estado=True
            camara.save()
        else:
            messages.error(request, f'Camara {camara.nombre} ya estaba encendida')
        return redirect('/')


    def apagarCamara(request, nombre):
        camara = Camara.objects.get(nombre=nombre)
        if camara.estado==True:
            options = {'THREADED_QUEUE_MODE': False}
            CamGear(source=camara.source,**options).stop()
            messages.success(request, f'Camara {camara.nombre} apagada')
            camara.estado=False
            camara.save()
        else:
            messages.error(request, f'Camara {camara.nombre} ya estaba apagada')
        return redirect('/')

class TelefonoView(View):

    def home(request):
        telefonoListados = Telefono.objects.all()
        messages.success(request, '¡Telefonos listados!')
        return render(request, "gestionTelefonos.html", {"Telefonos": telefonoListados})


    def registrarTelefono(request):
        numero = request.POST['numNumero']
        nombre = request.POST['txtNombre']
        chatid = request.POST['numChatid']
        telefono = Telefono.objects.create(
            numero=numero, nombre=nombre, chatid=chatid)
        messages.success(request, '¡Telefono registrado!')
        return redirect('/')


    def edicionTelefono(request, nombre):
        telefono = Telefono.objects.get(nombre=nombre)
        return render(request, "edicionTelefono.html", {"Telefono": telefono})


    def editarTelefono(request):
        numero = request.POST['numNumero']
        nombre = request.POST['txtNombre']
        chatid = request.POST['numChatid']

        telefono = Telefono.objects.get(nombre=nombre)
        telefono.numero = numero
        telefono.nombre = nombre
        telefono.chatid = chatid
        telefono.save()

        messages.success(request, '¡Telefono actualizado!')

        return redirect('/')


    def eliminarTelefono(request, nombre):
        telefono = Telefono.objects.get(nombre=nombre)
        telefono.delete()

        messages.success(request, '¡Telefono eliminado!')

        return redirect('/')

class HorarioView(View):

    def home(request):
        horarioListados = Horario.objects.all()
        messages.success(request, '¡Horario listados!')
        return render(request, "gestionHorario.html", {"Horarios": horarioListados})


    def registrarHorario(request):
        dia = request.POST['numDia']
        horainicio = request.POST['timeHoraIni']
        horafin = request.POST['timeHoraFin']
        horario = Horario.objects.create(
            dia=dia, horainicio=horainicio, horafin=horafin)
        messages.success(request, '¡Horario registrado!')
        return redirect('/')


    def edicionHorario(request, id):
        horario = Horario.objects.get(id=id)
        return render(request, "edicionHorario.html", {"Horario": horario})


    def editarHorario(request,id):
        dia = request.POST['numDia']
        horainicio = request.POST['timeHoraIni']
        horafin = request.POST['timeHoraFin']

        horario = Horario.objects.get(id=id)
        horario.dia = dia
        horario.horainicio = horainicio
        horario.horafin = horafin
        horario.save()

        messages.success(request, '¡Horario actualizado!')

        return redirect('/')


    def eliminarHorario(request, id):
        horario = Horario.objects.get(id=id)
        horario.delete()

        messages.success(request, '¡Horario eliminado!')

        return redirect('/')


class AlertaView(View):

    def home(request):
        alertaListados = Alerta.objects.all()
        messages.success(request, '¡Alertas listadas!')
        return render(request, "gestionAlerta.html", {"Alertas": alertaListados})


    def registrarAlerta(request):
        idCamtel = request.POST['numidCamtel']
        idFoto = request.POST['idFoto']
        alerta = Alerta.objects.create(
            idCamtel=idCamtel, idFoto=idFoto)
        messages.success(request, '¡Alerta registrada!')
        return redirect('/')


    def edicionAlerta(request, id):
        alerta = Alerta.objects.get(id=id)
        return render(request, "edicionAlerta.html", {"Alerta": alerta})


    def editarAlerta(request,id):
        idCamtel = request.POST['numidCamtel']
        idFoto = request.POST['idFoto']

        alerta = Alerta.objects.get(id=id)
        alerta.idCamtel = idCamtel
        alerta.idFoto = idFoto
        alerta.save()

        messages.success(request, '¡Alerta actualizada!')

        return redirect('/')


    def eliminarAlerta(request, id):
        alerta = Alerta.objects.get(id=id)
        alerta.delete()

        messages.success(request, '¡Alerta eliminada!')

        return redirect('/')


class FotoView(View):

    def home(request):
        fotoListados = Foto.objects.all()
        messages.success(request, '¡Fotos listadas!')
        return render(request, "gestionFoto.html", {"Fotos": fotoListados})


    def registrarFoto(request):
        path = request.POST['txtPath']
        camname = request.POST['txtCamname']
        foto = Foto.objects.create(
            path=path, camname=camname)
        messages.success(request, '¡Foto registrada!')
        return redirect('/')


    def edicionFoto(request, idFoto):
        foto = Foto.objects.get(idFoto=idFoto)
        return render(request, "edicionFoto.html", {"Foto": foto})


    def editarFoto(request,idFoto):
        path = request.POST['txtPath']
        camname = request.POST['txtCamname']

        foto = Foto.objects.get(idFoto=idFoto)
        foto.path = path
        foto.camname = camname
        foto.save()

        messages.success(request, '¡Foto actualizada!')

        return redirect('/')


    def eliminarFoto(request, idFoto):
        foto = Foto.objects.get(idFoto=idFoto)
        foto.delete()

        messages.success(request, '¡Foto eliminada!')

        return redirect('/')


    '''@method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def crear_camara(self, nombre, source):
        if not source:
            raise ValueError('Camara debe tener una direccion source')
        
        camara = self.model(nombre=nombre)
        camara = self.model(source=source)
        camara.save()
        return camara
    
    def get(self, request, id=0):
        if (id>0):
            camaras = list(Camara.objects.filter(id=id).values())
            if len(camaras)>0:
                cam=camaras[0]
                mensaje = {'message': "exitoso", 'camaras': cam}
            else:
                mensaje = {'message': "camara no encontrada"}
            return JsonResponse(mensaje)
        else:
            camaras = list(Camara.objects.values())
            if len(camaras) > 0:
                mensaje = {'message': "exitoso", 'camaras': camaras}
            else:
                mensaje = {'message': "camara no encontrada"}
            return JsonResponse(mensaje)

    def post(self, request):
        carga= json.loads(request.body.decode('utf-8'))
        Camara.objects.create(nombre=carga['nombre'],source=carga['source'])
        mensaje = {'message': "exitoso"}
        return JsonResponse(mensaje)

    def put(self, request, id=0):
        datos = json.loads(request.body)
        camaras = list(Camara.objects.filter(id=id).values())
        if len(camaras)>0:
            cam=Camara.objects.get(id=id)
            cam.nombre=datos['nombre']
            cam.source=datos['source']
            cam.save()
            mensaje = {'message': "exitoso"}
        else:
            mensaje = {'message': "camara no encontrada"}
        return JsonResponse(mensaje)
        

    def delete(self, request, id):
        camaras = list(Camara.objects.filter(id=id).values())
        if len(camaras)>0:
            Camara.objects.filter(id=id).delete()
            mensaje = {'message': "exitoso"}
        else:
            mensaje = {'message': "Camara no encontrada"}
        return JsonResponse(mensaje)

    
class TelefonoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            telefonos = list(Telefono.objects.filter(id=id).values())
            if len(telefonos)>0:
                tel=telefonos[0]
                mensaje = {'message': "exitoso", 'telefonos': tel}
            else:
                mensaje = {'message': "telefono no encontrado"}
            return JsonResponse(mensaje)
        else:
            telefonos = list(Telefono.objects.values())
            if len(telefonos) > 0:
                mensaje = {'message': "exitoso", 'telefonos': telefonos}
            else:
                mensaje = {'message': "telefono no encontrado"}
            return JsonResponse(mensaje)

    def post(self, request):
        carga= json.loads(request.body.decode('utf-8'))
        Telefono.objects.create(numero=carga['numero'],nombre=carga['nombre'],chatid=carga['chatid'])
        mensaje = {'message': "exitoso"}
        return JsonResponse(mensaje)

    def put(self, request, id=0):
        datos = json.loads(request.body)
        telefonos = list(Telefono.objects.filter(id=id).values())
        if len(telefonos)>0:
            tel=Telefono.objects.get(id=id)
            tel.nombre=datos['numero']
            tel.nombre=datos['nombre']
            tel.source=datos['chatid']
            tel.save()
            mensaje = {'message': "exitoso"}
        else:
            mensaje = {'message': "telefono no encontrado"}
        return JsonResponse(mensaje)
        

    def delete(self, request, id):
        telefonos = list(Telefono.objects.filter(id=id).values())
        if len(telefonos)>0:
            Telefono.objects.filter(id=id).delete()
            mensaje = {'message': "exitoso"}
        else:
            mensaje = {'message': "telefono no encontrado"}
        return JsonResponse(mensaje)
'''
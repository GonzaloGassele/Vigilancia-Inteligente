from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Camara, Skedul, Telefono, Horario, Alerta, Foto
from django.shortcuts import render, redirect
from django.contrib import messages
from vidgear.gears import CamGear
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AbstractUser, UserManager, User

def index(request):
    return HttpResponse("Hello, world. You're at the Vigilancia Inteligente index.")

def autenticar(request):
    username = request.POST['username']
    password = request.POST['password']
    usuario = authenticate(request, username=username, password=password)
    if usuario is not None:
        login(request, usuario)
        return redirect('/vibackend/telefono/')
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


############################################################
class TelefonoView(LoginRequiredMixin, View):
    login_url = '/vibackend/login/'
    redirect_field_name = 'redirect_to'

    def home(request):
        telefonoListados = Telefono.objects.filter(usertel=request.user)
        #messages.success(request, '¡Telefonos listados!')
        print(telefonoListados)
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
'''@login_required()
def home(request):
    telefonoListados = Telefono.objects.all()
    #messages.success(request, '¡Telefonos listados!')
    print(telefonoListados)
    return render(request, "gestionTelefonos.html", {'telefono': telefonoListados,})


def registrarTelefono(request):
    nombre = request.POST['txtNombre']
    numero = request.POST['txtNumero']
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    usertel = username
    telefono = Telefono.objects.create(
        nombre = nombre, numero = numero, usertel=usertel
    )
    return redirect('/vibackend/telefono/home')

def eliminarTelefono(request, idTelefono):
    telefono = Telefono.objects.get(idTelefono = idTelefono)
    telefono.delete()
    return redirect('/')

def edicionTelefono(request, idTelefono):
    telefono = Telefono.objects.get(idTelefono = idTelefono)
    return render(request, "edicionTelefono.html", {"telefono": telefono})

def editarTelefono(request):
    nombre = request.POST['txtNombre']
    numero = request.POST['txtNumero']
    idTelefono = request.POST['idTelefono']


    telefono = Telefono.objects.get(idTelefono = idTelefono)
    telefono.nombre = nombre
    telefono.numero = numero
    telefono.save()

    return redirect('/')'''
#####################################################################################

class HorarioView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

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


class AlertaView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

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


class FotoView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

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
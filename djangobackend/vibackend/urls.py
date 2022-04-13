from django.urls import path
from .views import CamaraView, HorarioView, AlertaView, FotoView, TelefonoView
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'vibackend'
urlpatterns = [
    path('index/', login_required(views.index)),
    path('index/prender/', login_required(views.prenderSistema)),
    path('index/apagar/', login_required(views.apagarSistema)),

    path('login/', views.loguear),
    path('autenticar/', views.autenticar),
    path('registrar/', views.registrar),
    path('autenticarRegistro/', views.autenticarRegistro),
    path('logout/', views.desloguear),

    path('camara/', login_required(CamaraView.home)),
    path('camara/registrarCamara/', login_required(CamaraView.registrarCamara)),
    path('camara/edicionCamara/<idCamara>', login_required(CamaraView.edicionCamara)),
    path('camara/editarCamara/', login_required(CamaraView.editarCamara)),
    path('camara/eliminarCamara/<idCamara>', login_required(CamaraView.eliminarCamara)),
    path('camara/apagarCamara/<idCamara>', login_required(CamaraView.apagarCamara)),
    path('camara/prenderCamara/<idCamara>', login_required(CamaraView.prenderCamara)),

    path('telefono/', login_required(TelefonoView.home)),
    path('telefono/registrarTelefono/', login_required(TelefonoView.registrarTelefono)),
    path('telefono/edicionTelefono/<idTelefono>', login_required(TelefonoView.edicionTelefono)),
    path('telefono/editarTelefono/', login_required(TelefonoView.editarTelefono)),
    path('telefono/eliminarTelefono/<idTelefono>', login_required(TelefonoView.eliminarTelefono)),

    path('horario/', login_required(HorarioView.home)),
    path('horario/editarHorario/', login_required(HorarioView.editarHorario)),

    path('alerta/', login_required(AlertaView.home)),
    path('alerta/fullTime/<idTelefono>/', login_required(AlertaView.fullTime)),
    path('alerta/editarAlerta/<idCamtel>', login_required(AlertaView.editarAlerta)),

    path('pruebaFoto/', login_required(FotoView.pruebaFoto), name = 'pruebaFoto'),
    path('pruebaFoto/confirmarFoto/<idFoto>/<confirmacion>/<pagina>', login_required(FotoView.confirmarFoto), name='confirmarFoto')
]
from django.urls import path
from .views import CamaraView, HorarioView, AlertaView, FotoView, TelefonoView
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'vibackend'
urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.loguear),
    path('autenticar/', views.autenticar),
    path('registrar/', views.registrar),
    path('autenticarRegistro/', views.autenticarRegistro),
    path('logout/', views.desloguear),

    path('camara/home', CamaraView.home, name='camaras_list'),
    path('camara/registrarCamara/', CamaraView.registrarCamara, name='camaras_register'),
    path('camara/edicionCamara/<nombre>', CamaraView.edicionCamara, name='camaras_edition'),
    path('camara/editarCamara/', CamaraView.editarCamara, name='camaras_edit'),
    path('camara/eliminarCamara/<nombre>', CamaraView.eliminarCamara, name='camaras_delete'),

    path('telefono/', login_required(TelefonoView.home)),
    path('telefono/registrarTelefono/', login_required(TelefonoView.registrarTelefono)),
    path('telefono/edicionTelefono/<idTelefono>', login_required(TelefonoView.edicionTelefono)),
    path('telefono/editarTelefono/', login_required(TelefonoView.editarTelefono)),
    path('telefono/eliminarTelefono/<idTelefono>', login_required(TelefonoView.eliminarTelefono)),

    path('horario/home/', HorarioView.home, name='horarios_list'),
    path('horario/registrarHorario/', HorarioView.registrarHorario, name='horarios_register'),
    path('horario/edicionHorario/<int:id>', HorarioView.edicionHorario, name='horarios_edition'),
    path('horario/editarHorario/<int:id>', HorarioView.editarHorario, name='horarios_edit'),
    path('horario/eliminarHorario/<int:id>', HorarioView.eliminarHorario, name='horarios_delete'),

    path('alerta/home', AlertaView.home, name='alertas_list'),
    path('alerta/registrarAlerta/', AlertaView.registrarAlerta, name='alertas_register'),
    path('alerta/edicionAlerta/<int:id>', AlertaView.edicionAlerta, name='alertas_edition'),
    path('alerta/editarAlerta/<int:id>', AlertaView.editarAlerta, name='alertas_edit'),
    path('alerta/eliminarAlerta/<int:id>', AlertaView.eliminarAlerta, name='alertas_delete'),

    path('foto/home', FotoView.home, name='fotos_list'),
    path('foto/registrarFoto/', FotoView.registrarFoto, name='fotos_register'),
    path('foto/edicionFoto/<int:id>', FotoView.edicionFoto, name='fotos_edition'),
    path('foto/editarFoto/<int:id>', FotoView.editarFoto, name='fotos_edit'),
    path('foto/eliminarFoto/<int:id>', FotoView.eliminarFoto, name='fotos_delete')
    
    #path('telefono/home/', views.home),
    #path('telefono/registrarTelefono/', views.registrarTelefono),
    #path('telefono/edicionTelefono/<nombre>', views.edicionTelefono),
    #path('telefono/editarTelefono/', views.editarTelefono),
    #path('telefono/eliminarTelefono/<nombre>', views.eliminarTelefono),
]
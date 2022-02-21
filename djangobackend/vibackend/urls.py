from django.urls import path
from .views import CamaraView, TelefonoView

from . import views

app_name = 'vibackend'
urlpatterns = [
    path('', views.index, name='index'),
    path('camara/', CamaraView.as_view(), name='camaras_list'),
    path('camara/<int:id>', CamaraView.as_view(), name='camaras_process'),
    path('telefono/', TelefonoView.as_view(), name='telefonos_list'),
    path('telefono/<int:id>', TelefonoView.as_view(), name='telefonos_process')
]
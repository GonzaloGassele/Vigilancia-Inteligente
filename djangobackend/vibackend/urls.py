from django.urls import path
from .views import CamaraView

from . import views

app_name = 'vibackend'
urlpatterns = [
    path('', views.index, name='index'),
    path('camara/', CamaraView.as_view(), name='camaras_list'),
]
from django.urls import path

from . import views

app_name = 'vibackend'
urlpatterns = [
    path('', views.index, name='index'),
]
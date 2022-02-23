from django.contrib import admin
from .models import Camara, Foto, Telefono, Skedul, Horario, Alerta, Camtel
from django import forms

class CustomFoto(forms.ModelForm):
    path = forms.CharField()

    class Meta:
        model = Foto
        fields = ('idFoto','etiqueta','camname',)

class FotoAdmin(admin.ModelAdmin):
    form = CustomFoto

admin.site.register(Horario)
admin.site.register(Skedul)
admin.site.register(Camara)
admin.site.register(Telefono)
admin.site.register(Camtel)
admin.site.register(Alerta)
admin.site.register(Foto, FotoAdmin)
#admin.site.register(Foto)
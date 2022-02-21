from django.contrib import admin
from .models import Usuario, Camara, Foto, Telefono, Skedul, Horario, Alerta, Camtel

admin.site.register(Usuario)
admin.site.register(Horario)
admin.site.register(Skedul)
admin.site.register(Camara)
admin.site.register(Telefono)
admin.site.register(Camtel)
admin.site.register(Alerta)
admin.site.register(Foto)
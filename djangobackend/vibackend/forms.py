from django import forms
  
class FechaForm(forms.Form):
    fecha = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M:%S',])
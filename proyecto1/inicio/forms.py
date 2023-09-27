from django import forms

class Crearuser(forms.Form):
    nombre = forms.CharField(label= 'Ingresa un nombre de usuario', max_length= 50, required=True)
    contraseña = forms.CharField(label= 'Escribe una contraseña (max. 16 caracteres)', max_length= 16, required=True)
    correo = forms.CharField(label= 'Ingresa tu correo electrónico', required=True)
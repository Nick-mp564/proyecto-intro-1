from django import forms

class Crearuser(forms.Form):
    email = forms.CharField(label= 'Ingresa tu correo electrónico', required=True)
    psw = forms.CharField(label= 'Escribe una contraseña (max. 16 caracteres)', max_length= 16, required=True)

class Publicacion(forms.Form):
    nombre =  forms.CharField(max_length=50)
    likes = forms.IntegerField()
    compartidos = forms.IntegerField()
    
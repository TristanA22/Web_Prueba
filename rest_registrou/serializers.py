from rest_framework import serializers
from core.models import Registrou
from django import forms

class RegistrouSerializer(serializers.ModelSerializer):
    
    password = forms.CharField(widget=forms.PasswordInput)
    telefono = forms.IntegerField(min_value =900000000,max_value=999999999) 


    class Meta:
        model = Registrou
        fields = ['n_identificacion', 'nombre_completo', 'telefono', 'direccion', 'email','password','pais']
  
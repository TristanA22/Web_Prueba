# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email, validate_slug
from django.forms import ModelForm
from .models import Registrou
from django import forms
from django.db import models
# from django.core.validators import RegexValidator



class RegistrousForm(ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)
    telefono = forms.IntegerField(min_value =900000000,max_value=999999999) 
   
  

    class Meta:
        model = Registrou
        fields = ['n_identificacion', 'nombre_completo', 'telefono', 'direccion', 'email','password','pais']
  

    # def clean_email(self):
    #     email_passed = self.cleaned_data.get('email')
    #     email_req = "gmail.com"
    #     if not email_req in email_passed:
    #         raise forms.ValidationError(" No es valido el email. Por favor intenta otra vez")
    #     return email_passed


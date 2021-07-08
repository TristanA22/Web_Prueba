from .models import Registrou
from core.forms import Registrou, RegistrousForm
from django.shortcuts import redirect, render

def Inicio(request):
   
    return render(request, 'core/Inicio.html')

def producto1(request):
   
    return render(request, 'core/producto1.html')

def producto2(request):
   
    return render(request, 'core/producto2.html')

def producto3(request):
   
    return render(request, 'core/producto3.html')

def formulario(request):
   
    return render(request, 'core/formulario.html')

def sismos(request):
   
    return render(request, 'core/sismos.html')

def quien(request):
   
 return render(request, 'core/quienessomos.html')

# Create your views here.
def home(request):
    registrous = Registrou.objects.all()
    datos = {
        "registrous" : registrous
    }
    return render(request, 'core/home.html', datos)
    
def form_registrous(request):
    datos = {
        'form' : RegistrousForm()
    }

    if request.method == 'POST':
        formulario = RegistrousForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/form_usuario.html', datos)


def form_mod_usuario(request, id):

    registrou = Registrou.objects.get(n_identificacion=id)

    datos = {
        'form' : RegistrousForm(instance=registrou)
    }

    if request.method == 'POST':
        formulario = RegistrousForm(request.POST, instance=registrou)
        if formulario.is_valid:
            formulario.save()
            datos['form'] = formulario
            datos['mensaje'] = "Modificados correctamente"

    return render(request, 'core/form_mod_usuario.html', datos)   

def form_del_usuario(request, id):

    registrou = Registrou.objects.get(n_identificacion=id)

    registrou.delete()
    
    return redirect(to="home")

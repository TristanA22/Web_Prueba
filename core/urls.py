from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home,form_del_usuario,form_mod_usuario,form_registrous,producto1,Inicio,producto2,producto3,sismos,quien,formulario

urlpatterns = [
    path('', Inicio, name="Inicio"),
    path('producto1', producto1, name="producto1"),
    path('producto2', producto2, name="producto2"),
    path('producto3', producto3, name="producto3"),
    path('quienessomos', quien, name="quienessomos"),
    path('sismos',sismos, name="sismos"),
    path('formulario',formulario, name="formulario"),
    path('home', home, name="home"),
    path('form-usuario', form_registrous, name="form_usuario"),
    path('form-mod-usuario/<id>', form_mod_usuario, name="form_mod_usuario"),
    path('form-del-usuario/<id>', form_del_usuario, name="form_del_usuario"),

    ]
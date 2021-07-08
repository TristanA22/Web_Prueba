from django.urls import path
from rest_registrou.views import lista_colaboradores,detalle_colaborador
from rest_registrou.viewsLogin import login
urlpatterns = [
    path('lista_colaboradores', lista_colaboradores, name="lista_colaboradores"),
    path('detalle_colaborador/<id>', detalle_colaborador, name="detalle_colaborador"),
    path('login', login, name="login"),
]
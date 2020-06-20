from django.urls import path
from .views import clicad, nova_pessoa

urlpatterns = [
    path('cadastro/', clicad),
    path('cad/', nova_pessoa, name="clientes"),

]
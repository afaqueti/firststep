from django.urls import path
from .views import clicad

urlpatterns = [
    path('cadastro/', clicad),

]
from django.urls import path
from .views import frontend

urlpatterns = [
    path('index/', frontend),
]
from django.forms import ModelForm
from .models import Pessoa

class Formpessoas(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome','apelido','sexo','email','cpf','cnpj','matricula']



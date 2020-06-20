from django.shortcuts import render
from .models import Pessoa
from .forms import Formpessoas


def clicad(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'clientes.html', {'pessoas': pessoas})


def nova_pessoa(request):
    form = Formpessoas(request.POST, None)
    return render(request, 'cadastro.html', {'form': form})

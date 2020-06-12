from django.db import models

#Clientes
class Pessoa(models.Model):
    SEXO_CHOICES = (
        ("F", "F"),
        ("M", "M")
    )
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=30, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    cpf = models.CharField(max_length=11,null=True,blank=True)
    cnpj = models.CharField(max_length=11, null=True, blank=True)
    matricula = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.nome
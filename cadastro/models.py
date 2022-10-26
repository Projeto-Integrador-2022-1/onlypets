from django.db import models

# Create your models here.
class Cadastro_Pessoa(models.Model):
    Nome = models.CharField(max_length=300)
    Sobrenome = models.CharField(max_length=300)
    Email = models.EmailField(max_length=300)
    Telefone = models.CharField(max_length=300)
    Senha = models.CharField(max_length=300)
    Confirmar_Senha = models.CharField(max_length=300)

    def __str__(self):
        return self.Nome

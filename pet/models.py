from django.db import models

# Create your models here.
class Cadastro_Pet(models.Model):
    Nome = models.CharField(max_length=300)
    Peso = models.CharField(max_length=300,blank=True,default='')
    Nascimento = models.CharField(max_length=300,blank=True,default='')
    Especie = models.CharField(max_length=300)
    Sexo = models.CharField(max_length=300)
    Raça = models.CharField(max_length=300)
    Pelagem = models.CharField(max_length=300)
    ImagemPet = models.ImageField('Foto do pet')
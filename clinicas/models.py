from os import link
from django.db import models

# Create your models here.
class Clinica(models.Model):
    nome = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.nome}'
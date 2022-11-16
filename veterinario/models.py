from django.contrib.auth.models import User 
from django.db import models

# Create your models here.
class Servico(models.Model):
    nome = models.CharField(max_length=300)
    preco = models.FloatField()
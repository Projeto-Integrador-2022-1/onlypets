from django.contrib.auth.models import User 
from django.db import models

# Create your models here.
class Servico(models.Model):
    nome = models.CharField(max_length=300)
    preco = models.CharField(max_length=300)
    seg = models.BooleanField()
    ter = models.BooleanField()
    qua = models.BooleanField()
    qui = models.BooleanField()
    sex = models.BooleanField()
    sab = models.BooleanField()
    horad = models.BooleanField()
    horat = models.BooleanField()
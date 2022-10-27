from enum import auto
from django.contrib.auth.models import User 
from django.db import models

# Create your models here.
class Cadastro_Pessoa(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Telefone = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username

from django.contrib.auth.models import User 
from django.db import models
from clinicas.models import Clinica
# Create your models here.
class Cadastro_Pessoa(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Telefone = models.CharField(max_length=300)
    Crmv = models.CharField(max_length=300)
    Clinica = models.ForeignKey(Clinica,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.username

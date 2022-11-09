from django.db import models

# Create your models here.
class Cartao(models.Model):
    NumeroCartao = models.CharField(max_length=300)
    NomeCartao = models.CharField(max_length=300)
    DataExpirar = models.DateField("Data de Expiração")
    CodCVV = models.CharField(max_length=300)
    Padrao = models.BooleanField("Usar como padrão",default=False)
    
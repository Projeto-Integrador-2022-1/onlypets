from django.contrib.auth.models import User 
from django.db import models
from django.core.exceptions import ValidationError

SERVIÇOS=(
    ('-','Escolha um Serviço'),
    ('ES','Exame de Sangue'),
    ('RD','Radiografia'),
    ('VC','Vacinação'),
    ('AG','Avaliação Geral'),
)
def sev_validator(valor):
    if valor == '-':
        raise ValidationError("Você não selecionou um serviço.")

# Create your models here.
class Servico(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='servico')
    serv = models.CharField(max_length=300,choices=SERVIÇOS,default='-',validators=[sev_validator])
    preco = models.DecimalField(max_digits=9999,decimal_places=2)
    seg = models.BooleanField()
    ter = models.BooleanField()
    qua = models.BooleanField()
    qui = models.BooleanField()
    sex = models.BooleanField()
    sab = models.BooleanField()
    horad = models.BooleanField()
    horat = models.BooleanField()
    def __str__(self):
        return f'{self.serv}'
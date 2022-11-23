from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def picture_directory_path(instance, filename):
    extension = filename.split(".")[-1]
    return f"foto_pets_{instance.id}/pet_pic.{extension}"

# Create your models here.
SEX_CHOICES = (
    ('-', 'Escolha o sexo do seu pet'),
    ('m', 'Macho'),
    ('f', 'Fêmea'),
)
def sex_validator(valor):
    if valor == '-':
        raise ValidationError("Você não selecionou o sexo do seu pet.")
        
PELAGE_CHOICES = (
    ('-', 'Escolha a pelagem do pet'),
    ('PCL', 'Pelo curto e liso'),
    ('PCD', 'Pelo curto e duro'),
    ('PLL', 'Pelo longo e liso'),
    ('PLO', 'Pelo londo e ondulado'),
    ('PD', 'Pelagem dupla'),
)
def pelo_validator(valor):
    if valor == '-':
        raise ValidationError("Você não selecionou o tipo de pelo")

class Cadastro_Pet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='pet')
    nome = models.CharField(max_length=300)
    peso = models.CharField(max_length=300,null=True,default='',blank=True)
    nascimento = models.CharField(max_length=300,blank=True,null=True,default='')
    especie = models.CharField(max_length=300)
    sexo = models.CharField(max_length=300, choices=SEX_CHOICES, default='-', validators=[sex_validator])
    raca = models.CharField(max_length=300)
    pelagem = models.CharField(max_length=300,choices=PELAGE_CHOICES,default='-', validators=[pelo_validator])
    imagemPet = models.ImageField('Foto do pet',null=True,blank=True,upload_to=picture_directory_path)
    def __str__(self):
        return f'{self.nome}'
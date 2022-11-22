from django.contrib.auth.models import User 
from django.db import models
from clinicas.models import Clinica
# Create your models here.
def picture_directory_path(instance, filename):
    extension = filename.split(".")[-1]
    return f"foto_vet_{instance.id}/vet_pic.{extension}"

class Cadastro_Pessoa(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='perfil')
    Telefone = models.CharField(max_length=300)
    Crmv = models.CharField(max_length=300,null=True,blank=True)
    Clinica = models.ForeignKey(Clinica,on_delete=models.CASCADE,null=True)
    imagemVet = models.ImageField('Foto do Veterinário',null=True,blank=True,upload_to=picture_directory_path)

    def __str__(self):
        return self.user.username

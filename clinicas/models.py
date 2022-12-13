from django.db import models
def picture_directory_path(instance, filename):
    extension = filename.split(".")[-1]
    return f"foto_clinica_{instance.id}/clinica_pic.{extension}"
# Create your models here.
class Clinica(models.Model):
    nome = models.CharField(max_length=300)
    imagemClinica = models.ImageField('Foto da clinica',null=True,blank=True,upload_to=picture_directory_path,default='clinica_default/default_pic.png')
    def __str__(self):
        return f'{self.nome}'
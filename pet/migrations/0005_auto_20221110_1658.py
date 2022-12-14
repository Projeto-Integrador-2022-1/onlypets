# Generated by Django 3.2.15 on 2022-11-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_auto_20221110_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro_pet',
            name='imagemPet',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto do pet'),
        ),
        migrations.AlterField(
            model_name='cadastro_pet',
            name='nascimento',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro_pet',
            name='peso',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]

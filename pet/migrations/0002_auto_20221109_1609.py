# Generated by Django 3.2.16 on 2022-11-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro_pet',
            name='Pelagem',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='cadastro_pet',
            name='Sexo',
            field=models.CharField(max_length=300),
        ),
    ]
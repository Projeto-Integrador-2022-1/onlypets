# Generated by Django 3.2.15 on 2022-11-10 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pet', '0003_auto_20221110_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro_pet',
            name='teste2',
        ),
        migrations.AddField(
            model_name='cadastro_pet',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cadastro_pet',
            name='sexo',
            field=models.CharField(choices=[('-', 'Escolha o sexo do seu pet'), ('m', 'Macho'), ('f', 'Fêmea')], default='-', max_length=300),
        ),
    ]

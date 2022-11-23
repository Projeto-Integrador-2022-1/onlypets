# Generated by Django 3.2.15 on 2022-11-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('preco', models.CharField(max_length=300)),
                ('seg', models.BooleanField()),
                ('ter', models.BooleanField()),
                ('qua', models.BooleanField()),
                ('qui', models.BooleanField()),
                ('sex', models.BooleanField()),
                ('sab', models.BooleanField()),
                ('horad', models.BooleanField()),
                ('horat', models.BooleanField()),
            ],
        ),
    ]
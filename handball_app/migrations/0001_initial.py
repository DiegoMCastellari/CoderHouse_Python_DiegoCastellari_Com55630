# Generated by Django 4.2.4 on 2023-08-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clubes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('arena', models.CharField(max_length=100)),
                ('liga', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('altura', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=100)),
                ('club', models.CharField(max_length=100)),
                ('estado_actividad', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ligas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
    ]

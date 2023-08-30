from django.db import models
from django.contrib.auth.models import User


class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    altura = models.IntegerField()
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    estado_actividad = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} - {self.club}, {self.nacionalidad}"
    
    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'


class Club(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    arena = models.CharField(max_length=100)
    liga = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}, {self.pais}"

    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubes'


class Liga(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.pais}"
    
    class Meta:
        verbose_name = 'Liga'
        verbose_name_plural = 'Ligas'
    

class Arena(models.Model):
    nombre = models.CharField(max_length=255)
    capacidad = models.IntegerField()
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.capacidad} pers.) - {self.ciudad}, {self.pais}"
    
    class Meta:
        verbose_name = 'Arena'
        verbose_name_plural = 'Arenas'


class Avatar(models.Model):
    imagen = models.ImageField(upload_to='avatares')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
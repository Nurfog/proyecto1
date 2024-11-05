from django.db import models

class usuario(models.Model):
    email = models.CharField(max_length=200, unique=True)
    nombres = models.CharField(max_length=150)
    paterno = models.CharField(max_length=100)
    materno = models.CharField(max_length=100)
    fono = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    direccion = models.CharField(max_length=300)
    comuna = models.SmallIntegerField(default=0)
    region = models.SmallIntegerField(default=0)
    genero = models.SmallIntegerField(default=0)
    colegio = models.SmallIntegerField(default=0)
    rol = models.SmallIntegerField(default=0)
    activo = models.BooleanField(default=True)
       

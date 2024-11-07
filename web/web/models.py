from django.db import models
from django.contrib.auth.models import User

class planestudios(models.Model):
    idplan = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class cursos(models.Model):
    idcurso = models.AutoField(primary_key=True,null=False)
    idplan = models.ForeignKey(planestudios, on_delete=models.CASCADE,null=False)
    nombre = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class bancopreguntas(models.Model):
    idpregunta = models.AutoField(primary_key=True,null=False)
    idcurso = models.ForeignKey(cursos, on_delete=models.CASCADE,null=False)
    idplan = models.ForeignKey(planestudios, on_delete=models.CASCADE,null=False)
    pregunta = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True,null=False)

    def __str__(self):
        return self.pregunta


class bancorespuestas(models.Model):
    idrespuesta = models.AutoField(primary_key=True,null=False)
    idpregunta = models.ForeignKey(bancopreguntas, on_delete=models.CASCADE,null=False)
    respuesta = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True,null=False)

    def __str__(self):
        return self.respuesta

    
class bancoresultados(models.Model):
    idresultado = models.AutoField(primary_key=True,null=False)
    idpregunta = models.ForeignKey(bancopreguntas, on_delete=models.CASCADE,null=False)
    idrespuesta = models.ForeignKey(bancorespuestas, on_delete=models.CASCADE,null=False)
    resultado = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True,null=False)

    def __str__(self):
        return self.resultado